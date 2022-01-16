<template>
    <div id="content" class="columns is-mobile is-vcentered" style="min-height: 80vh;">
        <div class="column is-third">
            <img src="../assets/savings.svg" style="position: absolute; bottom: 3.2rem; z-index: -1; left: 0;">
        </div>
        <div class="column">
        <!-- File Upload -->
            <div id='file-select' class="levels mt-4">
                <div class="file has-name is-boxed mb-2 level-item has-background-primar">
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
</template>

<script>
    const getFile = () => {
        return document.querySelector('.file-input').files.item(0);
    }
    const setFile = () => {
        const file = getFile();
        const fileLabel = document.querySelector('.file-name');
        console.log('hello');
        fileLabel.textContent = file.name;
    }
    const handleFile = () => {
        alert('Handling file ' + getFile().name);
        document.querySelector('#file-select').classList.add('is-hidden');
    }
    export default {
        methods: {
            getFile,
            setFile,
            handleFile,
        }
    }
</script>

<style>
    #file-select {
    }
</style>