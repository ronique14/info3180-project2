<template>
    <h2 class="pg-header" id="registerheader">Register New User</h2>
    <div class="card text-left" style="width: 48rem;" id="registercard">
        <div class="card-body">
           
            <form id= "RegisterForm" >
                <div class="row mb-2">
                    <div class="col-auto">
                        <div class="form-group">
                            <label for="username">Username</label>
                            <input name="username" v-model="username" placeholder="" class="form-control register-form">
                        </div>
                    </div>
                    <div class="col-auto">
                        <div class="form-group">
                            <label for="password">Password</label>
                            <input name="password" v-model="password" placeholder="" type="password" class="form-control register-form">
                        </div>
                    </div>
                </div>

                <div class="row mb-2">
                    <div class="col-auto">
                        <div class="form-group">
                            <label for="name">Full Name</label>
                            <input name="name" v-model="name" placeholder="" class="form-control register-form">
                        </div>
                    </div>
                    <div class="col-auto">
                        <div class="form-group">
                            <label for="email">Email</label>
                            <input name="email" v-model="email" placeholder="" class="form-control register-form">
                        </div>
                    </div>
                </div>
                
                <div class="row mb-1">
                    <div class="col-auto">
                        <div class="form-group">
                            <label for="location">Location</label>
                            <input name="location" v-model="location" placeholder="" class="form-control register-form">
                        </div>
                    </div>
                </div>

                <div class="form-group">
                    <label for="description">Biography</label>
                    <textarea name="description" v-model="description" id="description" class="mb-2 mr-sm-2 form-control" placeholder="Add Description"></textarea>
                </div>

                <div class="form-group">
                    <label for="photo">Upload Photo</label>
                    <input class="form-control register-form" type="file" id="photo" name="photo" @change="selectImage">
                </div>

                <br>

                <div class="col-12">
                    <button id="registerbtn" type="submit" name="submit" class="btn btn-primary" @click.prevent="register">Register</button>
                </div>
            </form>
        </div>
    </div>
</template>

<script>
export default {
    data() {
        return {
            csrf_token: '',
            username: '',
            password: '',
            name: '',
            email: '',
            location: '',
            description: '',
            photo: ''
        }
    },
    
    methods: {
        register(){
            let registerForm = document.getElementById('RegisterForm');
            let formdata = new FormData(registerForm);

            fetch("/api/register", {
                method: 'POST', 
                body: formdata,
                headers: {'X-CSRFToken': this.csrf_token}
            })
            
            .then(function (response) {
                console.log(response)
                return response.json();
            })

            .then(function (data) {
                // display a success message
                console.log("success")
                console.log(data);
            })

            .catch(function (error) {
                console.log(error);
            });
            
            this.$router.push('/explore');
        },

        getCsrfToken(){
            const user = this.$store.state.auth
            console.log(user)
            let self = this;
            fetch('/api/csrf-token')
            .then((response) => response.json())
            .then((data) => {
                console.log(data);
                self.csrf_token = data.csrf_token;
            })
        },
    }  
}
</script>

<style>
    #registerheader{
        font-size: 2em;
        font-weight: bold;
         text-align:center;
        margin-top:2% ;
        
        
        
    }
    
    .register-form {
        width: 350px;
    }
    body {
        background-color: #f3f4f6;
    }
    
    label {
        font-weight: bold;
        font-size: 0.8em;
    }

    #registerbtn{
        background-color: #0fb881;
        border: 1px solid transparent;
    }

    #registercard{
    display: block;
    margin-left: auto;
    margin-right: auto;
    margin-top: 2%;
    box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
    }
</style>