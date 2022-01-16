<template>
    <div id="table-container" class="containter is-hidden">
        <table width="100%" class="table is-fullwidth" style="font-size: 150%" id="dataTable">
            <thead>
                <tr>
                    <th>CPT Code</th>
                    <th>Service</th>
                    <th>Charge</th>
                    <th>Recieved</th>
                </tr>
            </thead>
            <tbody id="tableBody"></tbody>
        </table>
        <div class='box mt-6 has-background-success'>
            <p class="title has-text-white">You're total Possible Savings Are _______</p>
        </div>
    </div>
</template>
