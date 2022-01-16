<template>
    <div id="content" class="columns is-mobile is-vcentered" style="min-height: 80vh;">
        <div class="column is-third">
            <img src="../assets/savings.svg" style="position: absolute; bottom: 3.2rem; z-index: -1; left: 0;">
        </div>
        <div class="column">
        <!-- File Upload -->
            <div id='file-select' class="levels mt-4">
                <div class="file has-name is-boxed mb-2 level-item">
                    <label class="file-label">
                        <input class="file-input" type="file" name="resume" accept=".pdf" v-on:change="setFile()">
                        <span class="file-cta">
                        <span class="file-icon">
                            <i class="fas fa-upload"></i>
                        </span>
                        <span class="file-label">
                            Choose your bill...
                        </span>
                        </span>
                        <span class="file-name">
                        
                        </span>
                    </label>
                </div>
                <button id='file-submit' class="button is-primary ml-2" v-on:click="fileButtonPress()">Cick Me To Discover Your Savings!</button>
            </div>
        </div>
    </div>
    <!-- Table -->
    <app-table/>
</template>

<script>
    import AppTable from './AppTable.vue'
    import axios from 'axios'

    const getFile = () => {
        return document.querySelector('.file-input').files.item(0);
    }
    const setFile = () => {
        const file = getFile();
        const fileLabel = document.querySelector('.file-name');
        fileLabel.textContent = file.name;
    }
    const getNumber = (num) => {
        return num;
    }
    /* const handleFile = () => {
        document.querySelector('#content').classList.add('is-hidden');
        document.querySelector('#table-container').classList.remove('is-hidden');
        const data = [['80050', 'General health panel', '$201', '0'], 
                        ['84439', 'Thyroxine (thyroid chemical), free', '$55', '0'], 
                        ['83206', 'Vitamin D-3 Level', '$207', 0], 
                        ['80061', 'Blood Test, Lipids (cholesterol and triglycerides)', '$80', getNumber(0)], 
                        ['99396', 'Established patient periodic preventive medicine examination (40-64 years)', '$455', getNumber(5)]
                    ];
        console.log(data);
        //Parse PDF grabbing file with getFile() to get data
        generateTableRows(data);
    } */

    function getDescription(code) {
        let url = "https://us-central1-cruzhacks2022-338309.cloudfunctions.net/cpt_decription?code=" + code;
        return new Promise(function (resolve, reject) {
            axios.get(url).then(
                (response) => {
                    var result = response.data;
                    resolve(result);
                },
                    (error) => {
                    reject(error);
                }
            );
        });
    }
    function getDict(encodedPDF){
        let url = "https://us-central1-cruzhacks2022-338309.cloudfunctions.net/parsePDF";
        return new Promise(function (resolve, reject) {
            axios.post(url, { "pdf-data": encodedPDF }).then(response => {
                var result = response.data;
                resolve(result);
            }, 
                (error) => {
                    reject(error);
                })
        });
    }

    async function fileButtonPress(){
        document.querySelector('#content').classList.add('is-hidden');
        // show loading screen

        // We need to parse the pdf
        // We need to get the file that the user inputted
        console.log(getFile())

        var reader = new FileReader();
        //var codePrices = {}
        let res = null;
        reader.onload=function(){
            res = btoa(reader.result);
            //console.log(res);
            //console.log(await getDict2(res));
            console.log(getDict(res));
        }
        
        reader.readAsBinaryString(getFile());

        //console.log(await getDict2(res));

        const data = [['80050', await getDescription('84439'), '$201', '0'], 
                        ['84439', await getDescription('84439'), '$55', '0'], 
                        ['83206', await getDescription('84439'), '$207', 0], 
                        ['80061', await getDescription('84439'), '$80', getNumber(0)], 
                        ['99396', await getDescription('84439'), '$455', getNumber(5)]
                    ];
        generateTableRows(data);
        
        document.querySelector('#table-container').classList.remove('is-hidden');
    }

    function generateTableRows(data) {
        
        const tableBody = document.querySelector('#tableBody');
        data.forEach((item) => {
            const row = document.createElement('tr');
            for(let i = 0; i < 4; i++){
                const cell = document.createElement('td');
                cell.textContent = item[i];
                row.append(cell);
            }
            /* Add Checkbox */
            const input = document.createElement('input');
            input.setAttribute('type', 'checkbox');
            input.classList.add('checkbox');
            row.append(input);
            tableBody.append(row);
        });
    }
    export default {
        components: {
            AppTable,
        },
        methods: {
            getFile,
            setFile,
            fileButtonPress,
            generateTableRows,
        }
    }
</script>
