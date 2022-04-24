<template>
    <h2 class="pg-header" id="pheader">Add New Car</h2>
    <div class="card text-left" style="width: 48rem;" id="card">
        <div class="card-body">
            <form id="NewCar" >
                <div class="row mb-2">
                    <div class="col-auto">
                        <div class="form-group">
                            <label for="make">Make</label>
                            <input name="make" v-model="make" placeholder="Make" class="form-control register-form">
                        </div>
                    </div>
                    <div class="col-auto">
                        <div class="form-group">
                            <label for="model">Model</label>
                            <input name="model" v-model="model" placeholder="Model" class="form-control register-form">
                        </div>
                    </div>
                </div>

                <div class="row mb-2">
                    <div class="col-auto">
                        <div class="form-group">
                            <label for="colour">Colour</label>
                            <input name="colour" v-model="colour" placeholder="Colour" class="form-control register-form">
                        </div>
                    </div>
                    <div class="col-auto">
                        <div class="form-group">
                            <label for="year">Year</label>
                            <input name="year" v-model="year" placeholder="2022" class="form-control register-form">
                        </div>
                    </div>
                </div>

                <div class="row mb-2">
                    <div class="col-auto">
                        <div class="form-group">
                            <label for="price">Price</label>
                            <input name="price" v-model="price" placeholder="$" class="form-control register-form">
                        </div>
                    </div>
                    <div class="col-auto">
                        <div class="form-group">
                            <label for="type">Car Type</label>
                            <select name="type" id="cars" class="form-select register-form">
                                <option value="coupe">Coupe</option>
                                <option value="hat">Hatchback</option>
                                <option value="sedan">Sedan</option>
                                <option value="super">Supercar</option>
                                <option value="suv">SUV</option>
                            </select>
                        </div>
                    </div>
                </div>

                <div class="row mb-1">
                    <div class="col-auto">
                        <div class="form-group">
                            <label for="transmission">Transmission</label>
                            <select name="transmission" id="transmission" class="form-select register-form">
                                <option value="automatic">Automatic</option>
                                <option value="manual">Manual</option>
                            </select>
                        </div>
                    </div>
                </div>

                <div class="form-group">
                    <label for="description">Description</label>
                    <textarea name="description" v-model="description" id="description" class="mb-2 mr-sm-2 form-control" placeholder="Add Description"></textarea>
                </div>

                <div class="form-group">
                    <label for="photo">Upload Photo</label>
                    <input class="form-control register-form" type="file" id="photo" name="photo" @change="selectImage">
                </div>

                <br>

                <div class="col-12">
                    <button id="btn1" typve="submit" name="submit" class="btn btn-primary" @click.prevent="save">Save</button>
                </div>
            </form>
        </div>
    </div>
</template>

<script>
export default{
    data() {
        return {
            csrf_token: '',
            make: '',
            model: '',
            colour: '',
            year: '',
            price: '',
            type: '',
            transmission: '',
            description: '',
            photo:''          
        }
    },

}
</script>

<style>
    .pg-header{
        font-size: 2em;
    }

    .register-form {
        width: 350px;
    }

    label {
        font-weight: bold;
        font-size: 0.8em;
    }
</style>