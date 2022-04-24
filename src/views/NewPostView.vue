<template>
    <div class="newcar container">
        <NewCarForm/>
    </div>
</template>

<script>
import NewCarForm from '../components/NewCarForm.vue'

export default({
    data() {
        return{
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
    components: { NewCarForm }
})
</script>