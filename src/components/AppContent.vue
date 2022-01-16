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
                <button id='file-submit' class="button is-primary ml-2" v-on:click="handleFile()">Cick Me To Discover Your Savings!</button>
            </div>
        </div>
    </div>
    <!-- Table -->
    <app-table/>
</template>

<script>
    import AppTable from './AppTable.vue'

    const getFile = () => {
        return document.querySelector('.file-input').files.item(0);
    }
    const setFile = () => {
        const file = getFile();
        const fileLabel = document.querySelector('.file-name');
        fileLabel.textContent = file.name;
    }
    const handleFile = () => {
        document.querySelector('#content').classList.add('is-hidden');
        document.querySelector('#table-container').classList.remove('is-hidden');
        const data = [['80050', 'General health panel', '$201'], 
                        ['84439', 'Thyroxine (thyroid chemical), free', '$55'], 
                        ['83206', 'Vitamin D-3 Level', '$207'], 
                        ['80061', 'Blood Test, Lipids (cholesterol and triglycerides)', '$80'], 
                        ['99396', 'Established patient periodic preventive medicine examination (40-64 years)', '$455']
                    ];
        console.log(data);
        generateTableRows(data);
    }
    function generateTableRows(data) {
        const tableBody = document.querySelector('#tableBody');
        data.forEach((item) => {
            const row = document.createElement('tr');
            for(let i = 0; i < 3; i++){
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
            handleFile,
            generateTableRows,
        }
    }
</script>
