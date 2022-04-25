<template>
    <h2 class="pg-header" id="exploreheader">Explore</h2>
    <div class="card text-left" style="width: 40rem;" id="explorecard">
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
                        <button id="searchbtn" type="submit" name="submit" class="btn btn-primary" @click.prevent="search">Search</button>
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

    #exploreheader{
        font-size: 2em;
        font-weight: bold;
        text-align:center;
        margin-top:2% ;
      }

 #explorecard{
    display: block;
    margin-left: auto;
    margin-right: auto;
    margin-top: 2%;
    box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
    }

     #searchbtn{
        background-color: #0fb881;
        border: 1px solid transparent;
        width:400%;
    }

</style>