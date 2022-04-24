<template>
    <div class="profile-container">
        <div class="card flex-row"  style="width: 45rem">
            <img class="card-img-sm-left profilepic" v-bind:src="'/uploads/' + user.photo" alt="Profile Picture" width="140" height="140">
            <div class="card-body">
                <h5  class="card-title">{{ user.name }}</h5>
                <p>@{{ user.username }}</p>
                <br>
                <p>{{ user.biography }}</p>
                <p>Email {{ user.email }}</p>
                <p>Location {{ user.location}}</p>
                <p>Joined {{ user.date_joined }}</p>  
            </div>
        </div>
        
        <br>

        <h2 class="fav_cars">Cars Favourited</h2>

        <br>
    </div>
</template>

<script>
export default {
    data(){
        return{
            user: ''
        }
    },
}
</script>

<style>
    
</style>