<template>
    <table width="100%" class="table" style="font-size: 150%">
        <thead>
            <tr>
                <th>CPT Code</th>
                <th>Service</th>
                <th>Charge</th>
                <th>Recieved?</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>80050</td>
                <td>General Health Panel</td>
                <td>$201</td>
                <td>
                    <label class="checkbox mr-5">
                        <input type="checkbox">
                        Yes
                    </label>
                    <spacer type="horizontal" width="200">
                    </spacer>
                    <label class="checkbox">
                        <input type="checkbox">
                        No
                    </label>
                </td>
            </tr>
            <tr>
                <td>84439</td>
                <td>Thyroxine (thyroid chemical), free</td>
                <td>$55</td>
                <td>
                    <label class="checkbox mr-5">
                        <input type="checkbox">
                        Yes
                    </label>
                    <spacer type="horizontal" width="200">
                    </spacer>
                    <label class="checkbox">
                        <input type="checkbox">
                        No
                    </label>
                </td>
            </tr>
            <tr>
                <td>83206</td>
                <td>Vitamin D-3 Level</td>
                <td>$207</td>
                <td>
                    <label class="checkbox mr-5">
                        <input type="checkbox">
                        Yes
                    </label>
                    <spacer type="horizontal" width="200">
                    </spacer>
                    <label class="checkbox">
                        <input type="checkbox">
                        No
                    </label>
                </td>
            </tr>
            <tr>
                <td>80061</td>
                <td>Blood Test, Lipids (cholesterol and triglycerides)</td>
                <td>$80</td>
                <td>
                    <label class="checkbox mr-5">
                        <input type="checkbox">
                        Yes
                    </label>
                    <spacer type="horizontal" width="200">
                    </spacer>
                    <label class="checkbox">
                        <input type="checkbox">
                        No
                    </label>
                </td>
            </tr>
            <tr>
                <td>99396</td>
                <td>Established patient periodic preventive medicine examination (40-64 years)</td>
                <td>$455</td>
                <td>
                    <label class="checkbox mr-5">
                        <input type="checkbox">
                        Yes
                    </label>
                    <spacer type="horizontal" width="200">
                    </spacer>
                    <label class="checkbox">
                        <input type="checkbox">
                        No
                    </label>
                </td>
            </tr>
        </tbody>
    </table>
</template>

<script>
export default {
    /*data: {
        services: [["80050", "General health panel", "$201"], 
                    ["84439", "Thyroxine (thyroid chemical), free", "$55"], 
                    ["83206", "Vitamin D-3 Level", "$207"], 
                    ["80061", "Blood Test, Lipids (cholesterol and triglycerides)", "$80"], 
                    ["99396", "Established patient periodic preventive medicine examination (40-64 years)", "$455"]
        ]
    },*/
    methods: {
        populate() {
        },
    }
}
</script>