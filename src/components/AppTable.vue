<template>
    <div class="containter">
        <table width="100%" class="table" style="font-size: 150%" id="dataTable">
            <thead>
                <tr>
                    <th>CPT Code</th>
                    <th>Service</th>
                    <th>Charge</th>
                    <th>Recieved?</th>
                </tr>
            </thead>
            <tbody id="tableBody">
                <tr v-for="(service, index) in services" :key="index">
                    <td>{{service[0]}}</td>
                    <td>{{service[1]}}</td>
                    <td>{{sercive[2]}}</td>
                    <td>
                        <label class="checkbox mr-5">
                            <input type="checkbox">
                            Yes
                        </label>
                    </td>
                </tr>
            </tbody>
        </table>
    </div>
</template>

<script>
export default {
    data() {
        return{
            services: [['80050', 'General health panel', '$201'], 
                        ['84439', 'Thyroxine (thyroid chemical), free', '$55'], 
                        ['83206', 'Vitamin D-3 Level', '$207'], 
                        ['80061', 'Blood Test, Lipids (cholesterol and triglycerides)', '$80'], 
                        ['99396', 'Established patient periodic preventive medicine examination (40-64 years)', '$455']
            ]
            /*services: [{CPT: '80050', service: 'General health panel', charge: '$201'}, 
                        {CPT: '84439', service: 'Thyroxine (thyroid chemical), free', charge: '$55'}, 
                        {CPT: '83206', service: 'Vitamin D-3 Level', charge: '$207'}, 
                        {CPT: '80061', service: 'Blood Test, Lipids (cholesterol and triglycerides)', charge: '$80'}, 
                        {CPT: '99396', service: 'Established patient periodic preventive medicine examination (40-64 years)', charge: '$455'}
            ]*/
        };
    }

    /*
    methods: {
        ServiceDict: {80050: "General health panel", 84439 : "Thyroxine (thyroid chemical), free", 83206: "Vitamin D-3 Level", 80061: "Blood Test, Lipids (cholesterol and triglycerides)", 99396: "Established patient periodic preventive medicine examination (40-64 years)"}
        ChargeDict: {80050: 201, 84439 : 55, 83206: 207, 80061: 80, 99396: 455}
        populate(ServiceDict, ChargeDict) {
            const data = []
            for(const [key, value] of Object.entries(ServiceDict)){
                data.push([key.toString(), value, "$" + ChargeDict[key].toString()])
            }
            
            data.forEach(function(item, index){
                var row = document.createElement('tr');
                var c1 = document.createElement('td');
                var c2 = document.createElement('td');
                var c3 = document.createElement('td');
                var c4 = document.createElement('td');
                var l1 = document.createElement('label');
                var i1 = document.createElement('input');

                l1.classList.add('checkbox');
                i1.classList.add('checkbox');

                l1.textContent = "Yes";
                l1.appendChild(i1);

                c4.appendChild(l1);
                
                c1.textContent = item[0];
                c2.textContent = item[1];
                c3.textContent = item[2];

                row.appendChild(c1);
                row.appendChild(c2);
                row.appendChild(c3);
                row.appendChild(c4);

                tableBody.appendChild(row);
            })

        },
    }*/
};
</script>
