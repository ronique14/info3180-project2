<template>
    <div class="register container">
        <RegisterForm/>
    </div>
</template>

<script>
import RegisterForm from '../components/RegisterForm.vue'

export default({
    data() {
        return{
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
    components: { RegisterForm }
})
</script>
