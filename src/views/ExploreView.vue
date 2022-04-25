<template>
    <div class="explore-container">
        <ExploreForm/>
    </div>
</template>

<script>
import ExploreForm from '../components/ExploreForm.vue'

export default({
    data() {
        return{
            make: '',
            model: '',

        }        
    },
    components: { ExploreForm }
})
</script>

<style>

</style>