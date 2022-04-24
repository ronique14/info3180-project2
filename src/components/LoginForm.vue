<template>
    <h2 class="pg-header" id="pheader">Login to your account</h2>
    <div class="card text-left" style="width: 25rem;" id="card">
        <div class="card-body">
            <form id= "RegisterForm" >
                <div class="col-auto">
                    <div class="form-group">
                        <label for="username">Username</label>
                        <input name="username" v-model="username" placeholder="Username" class="form-control register-form">
                    </div>
                </div>
                <div class="col-auto">
                    <div class="form-group">
                        <label for="password">Password</label>
                        <input name="password" v-model="password" placeholder="Password" type="password" class="form-control register-form">
                    </div>
                </div>

                <br>

                <div class="col-12">
                    <button id="btn1" type="submit" name="submit" class="btn btn-primary" @click.prevent="login">Login</button>
                </div>
            </form>
        </div>
    </div>
</template>

<script>
// import store from '@/main.js'; 

export default {
    data() {
        return {
            csrf_token: '',
            username: '',
            password: ''     
        }
    },
    
    methods: {
        login(){
            console.log()
            let loginForm = document.getElementById('LoginForm');
            let formdata = new FormData(loginForm);

            fetch("/api/auth/login", {
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
                if(data.token != ''){
                    localStorage.setItem('token', data.token );
                    localStorage.setItem('id', data.id);
                    store.commit('checkiftrue', true);
                    store.commit('checkid', data.id );
                }
                
                else{
                    localStorage.setItem('token', null );
                    localStorage.setItem('id', null );
                    store.commit('checkiftrue', false);
                }

                localStorage.setItem('auth', data.auth );
                console.log("shows check :", store.state.check, store.state.uid)
                console.log("token in local storage",localStorage.getItem('id'))
                console.log(data.token, data.id,localStorage.getItem('auth') );

                return(data);
            })

            .catch(function (error) {
                console.log(error);
            });

            this.$router.push('/');

        },

        getCsrfToken(){
            console.log("logged state",this.$store.state.auth)
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
    .login{
        margin-top: 10rem;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
    }

    .pg-header{
        font-size: 2em;
    }

    label{
        font-weight: bold;
        font-size: 0.8em;
    }
</style>