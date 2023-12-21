<template>
  <div class="app-wrapper">
    <NavBar v-if="isAuthenticated && role == 'Student'" />
    <ProfNavBar v-if="isAuthenticated && role == 'Professor'" />
    <AdminNavBar v-if="isAuthenticated && role == 'Admin'" />
    <RouterView  class="main"/>
  </div>
</template>

<script setup> 
import { ref, onMounted, watch, computed } from 'vue';
import { RouterView } from 'vue-router';
import { useAuth0 } from '@auth0/auth0-vue';
import { createAWSUser, getUser, addAuth0UserRoles } from '@/util/apiCaller'

import NavBar from './components/NavBar.vue';
import ProfNavBar from './components/ProfNavBar.vue';
import AdminNavBar from './components/AdminNavBar.vue';
import Home from './views/general/Home.vue'
import { useStore } from 'vuex';

const store = useStore();

const { isAuthenticated, idTokenClaims, getAccessTokenSilently } = useAuth0();
const claims = ref(idTokenClaims);
// const role = ref(store.state.userRole);
const role = computed(() => store.state.userRole);


// watch([role], async ([newRole]) => {
//   console.log(newRole);
// });

</script>

<style>

/* Fonts */
@import url('https://fonts.googleapis.com/css?family=Roboto+Condensed');
@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@100;400;700;800;900&family=Roboto:wght@100;200;300&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Roboto&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Roboto&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Montserrat:wght@400;700;800;900&family=Roboto&display=swap');

/* website level color & size variables */
:root {
  --primary: #F4EDEA;
  --sidebar: #12263A;
  --primary-blue: #00141F;
  --accent-grey: #a0a0a0;
  --accent-orange: #ffc400;
  --accent-red: #ff7070;
  --accent-orange-hover: #dfac04;
  --accent-b-orange: #ff9100;
  --accent-b-orange-hover: #d67900;
  --course-header: #21476d;
  --sidebar-hover: #F4EDEA;
  --sidebar-width: 15rem;
  --sidebar-text-color: #F4EDEA;
  --studentadmin-green: rgb(182,209,146);


  --auth0: #635dff;
}

/* :root {
  --primary: #FFFCF9;
  --sidebar: #353535;
  --accent-grey: #a0a0a0;
  --accent-orange: #FE5F55;
  --accent-orange-hover: #FE5F55;
  --accent-b-orange: #FE5F55;
  --accent-b-orange-hover: #FE5F55;
  --course-header: #21476d;
  --sidebar-hover: var(--primary);
  --sidebar-width: 15rem;
  --sidebar-text-color: #F4EDEA;
} */

.app-wrapper {
  display: flex;
  background-color: var(--primary);
  max-height: 100vh;
  min-height: 100vh;
}

.app-wrapper .main {
    flex: 1 1 0;
    align-items: center;
    margin-top: 0rem;
    padding: 0rem;
    font-family: "Roboto";
}

/* only apply margins to pages that are not the home page */
.app-wrapper .main:not(.home) {
  padding: 1rem;
}


</style>