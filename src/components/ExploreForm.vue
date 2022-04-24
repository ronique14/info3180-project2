<template>
    <h2 class="pg-header" id="pheader">Explore</h2>
    <div class="card text-left" style="width: 40rem;" id="card">
        <div class="card-body">
            <form id= "ExploreForm" >
                <div class="row mb-2">
                    <div class="col-auto">
                        <div class="form-group">
                            <label for="make">Make</label>
                            <input name="make" v-model="make" placeholder="Make" class="form-control explore-form">
                        </div>
                    </div>
                    <div class="col-auto">
                        <div class="form-group">
                            <label for="model">Model</label>
                            <input name="model" v-model="model" placeholder="Model" type="model" class="form-control explore-form">
                        </div>
                    </div>
                    <div class="col-1">
                        <label for="search"></label>
                        <button id="btn1" type="submit" name="submit" class="btn btn-primary" @click.prevent="search">Search</button>
                    </div>
                </div>
            </form>
        </div>
    </div>
</template>

<script>
export default {
    data() {
        return {
            
        };
    },

    
}
</script>

<style>

</style>