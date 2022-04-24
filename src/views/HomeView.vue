<script>
export default {
    data() {
        return {
            message: "Hello World! This is Lab 7"
        };
    },
}
</script>

<template>
       <div class="con">
    <div class="homepage">
      <div id="text">
        <h2>Buy and Sell <br> Cars Online</h2>
        <p>United Auto Sales provies the fastest easiest firendly way to buy or sell cars online. Find a Great Price on the Vehicle on the Vehicle You Want.</p>
        <div class="bttn">
          <RouterLink type="button" class="btn btn-primary" id="btn1" to="/register">Register</RouterLink>
          <RouterLink type="button" class="btn btn-success" id="btn2" to="/login">Login</RouterLink>
        </div>
        
      </div>
      <div id="car">
        <img class="sideimage" src="../img/Car.jpg" alt="">
      </div>
    </div>
  </div>
</template>

<style>
/* Add any component specific styles here */
  h2 {
    font-size: 6em;
  }

  p {
    margin-right: 88px;
    color: gray;
  }
 

  .homepage {
    display: flex;
    align-items: center;
    justify-content: center;
  }
  
  .sideimage {
    height: calc(98vh - 53px);
  }

  #text {
    padding-left: 8em;
  }

  body{
    padding-top: 53px;
    background-color: white;
  }

  #btn1{
     color: white;
     background-color: #3c81f6;
    margin-right: 8px;
  }

  #btn2{
     color: white;
     background-color:#0fb881;
    margin-right: 8px;
  }
</style>