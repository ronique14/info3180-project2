<template>
    <div class="login container">
        <LoginForm/>
    </div>
</template>

<script>
import LoginForm from '../components/LoginForm.vue'

export default({
    data() {
        return{
            csrf_token: '',
            username: '',
            password: ''
        }        
    },
    components: { LoginForm }
})
</script>
