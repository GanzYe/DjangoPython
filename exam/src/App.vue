<template>
  <div>
    <Nav/>
    <div class="newscontent">
      <router-view></router-view>
    </div>
  </div>
</template>

<script>
import Nav from './components/Nav.vue'

export default {
  name: 'App',
  components: {
    Nav,    
  }
  
}
</script>

<style> 
@import '/assets/static/assets/css/oneui.min.css';
body{
  background-color: rgb(211, 215, 226);
}
.newscontent{
  padding: 15px 180px 15px 180px;
  font-size: 14.4px;
  color:black;
}
</style>
