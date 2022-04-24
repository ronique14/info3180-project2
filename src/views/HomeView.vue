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
      <div id="side">
        <img class="sideimage" src="../images/sideimage.jpg" alt="">
      </div>
    </div>
  </div>
</template>

<style>
/* Add any component specific styles here */
  h2 {
    font-size: 6em;
    font-weight:600;
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
    height: calc(100vh - 53px);
  }

  #text {
    padding-left: 8em;
  }

  body{
    padding-top: 53px;
    background-color: white;
  }

<<<<<<< HEAD
   .registerbtn{
    padding: 15px 38px;
    border-radius: 10px;
    border: 1px solid transparent;
    width: 180px;
    font-size: 16px;
    letter-spacing: 1px;
    transition: all 0.15s linear;
    color: white;
    background-color: #3c81f6;
    margin-right: 14px;
    margin-top: 10px;
   
  }

  .loginbtn{
    padding: 15px 38px;
    border-radius: 10px;
    border: 1px solid transparent;
    width: 180px;
    font-size: 16px;
    letter-spacing: 1px;
    transition: all 0.15s linear; 
    color: white;
    background-color:#0fb881;
     
  }

  .loginbtn:hover{
    background-color: rgba(29, 201, 160, 0.08);
    border-color: #0fb881;
    color: #0fb881;
    transform: translateY(-5px) scale(1);

  }

  .registerbtn:hover{
    background-color: rgba(29, 201, 160, 0.08);
    border-color: #3c81f6;
    color: #3c81f6;
    transform: translateY(-5px) scale(1);

=======
  #btn1{
     color: white;
     background-color: #3c81f6;
    margin-right: 8px;
  }

  #btn2{
     color: white;
     background-color:#0fb881;
    margin-right: 8px;
>>>>>>> b00e9472f4107c405795051e9cfe2f36573cc7eb
  }
</style>