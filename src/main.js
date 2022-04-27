import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import { createStore } from 'vuex'

 
const store = createStore({
    state(){
        return{
            token: localStorage.getItem('token') || null,
            id: localStorage.getItem('id') || null,
            auth: localStorage.getItem('auth') || false,
            check: '',
            uid: '',
            pa: '',
            count: false,
        }
  
    },
    mutations:{
      checktrue(state, auth){
         state.check= auth
         
      },
      checkid(state, id){
        state.uid = id
      },
      getpath(state, pat){
        state.pa = pat
      },
      addcount(state){
        if(store.state.check == '' && store.state.count !== false){
          state.count= true
        }else{
          state.count= false
        }
  
      },
  
  },
  
  });

 

const app = createApp(App)
 

app.use(router)
app.use(store)
app.mount('#app')
export default store
