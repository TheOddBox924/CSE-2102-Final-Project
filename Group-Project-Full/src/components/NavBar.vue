<template>
  <aside>
    <div class="title">
      <h1>Syllabus Sync</h1>
      <hr> 
    </div>
    <div class="menu">

      <RouterLink class="menu-button" :class="{ active: (isActiveRoute === '/searchcourses') || (isActiveRoute === '/courseinfo')}"  to="/searchcourses">
        <svg class="icon" width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
          <path class="stroke" d="M18 3.00001V3.00001C19.6569 3.00001 21 4.34315 21 6.00001L21 8.14286C21 8.47698 21 8.64405 20.9234 8.76602C20.8834 8.82962 20.8296 8.8834 20.766 8.92336C20.644 9 20.477 9 20.1429 9L15 9M18 3.00001V3.00001C16.3431 3.00001 15 4.34315 15 6.00001L15 9M18 3.00001L7 3.00001C5.11438 3.00001 4.17157 3.00001 3.58579 3.58579C3 4.17158 3 5.11439 3 7.00001L3 21L6 20L9 21L12 20L15 21L15 9" stroke="#D6D6D6" stroke-width="2"/>
          <path class="stroke" d="M7 7L11 7" stroke="#D6D6D6" stroke-width="2" stroke-linecap="round"/>
          <path class="stroke" d="M8 11H7" stroke="#D6D6D6" stroke-width="2" stroke-linecap="round"/>
          <path class="stroke" d="M7 15L10 15" stroke="#D6D6D6" stroke-width="2" stroke-linecap="round"/>
        </svg>
        <span class="text">Search Courses</span>
      </RouterLink>

      <RouterLink class="menu-button" :class="{ active: isActiveRoute === '/managecourses' }" to="/managecourses">
        <svg class="icon" width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
          <path class="stroke" d="M20 12V17C20 18.8856 20 19.8284 19.4142 20.4142C18.8284 21 17.8856 21 16 21H6.5C5.11929 21 4 19.8807 4 18.5V18.5C4 17.1193 5.11929 16 6.5 16H16C17.8856 16 18.8284 16 19.4142 15.4142C20 14.8284 20 13.8856 20 12V7C20 5.11438 20 4.17157 19.4142 3.58579C18.8284 3 17.8856 3 16 3H8C6.11438 3 5.17157 3 4.58579 3.58579C4 4.17157 4 5.11438 4 7V18.5" stroke="#D6D6D6" stroke-width="2"/>
          <path class="stroke" d="M9 8L15 8" stroke="#D6D6D6" stroke-width="2" stroke-linecap="round"/>
        </svg>
        <span class="text">Manage Courses</span>
      </RouterLink>

      <RouterLink class="menu-button" :class="{ active: isActiveRoute === '/schedule' }" to="/schedule">
        <svg class="icon" width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
          <rect class="stroke" x="3" y="6" width="18" height="15" rx="2" stroke="#D6D6D6" stroke-width="2"/>
          <path class="fill" d="M3 10C3 8.11438 3 7.17157 3.58579 6.58579C4.17157 6 5.11438 6 7 6H17C18.8856 6 19.8284 6 20.4142 6.58579C21 7.17157 21 8.11438 21 10H3Z" fill="#D6D6D6"/>
          <path class="stroke" d="M7 3L7 6" stroke="#D6D6D6" stroke-width="2" stroke-linecap="round"/>
          <path class="stroke" d="M17 3L17 6" stroke="#D6D6D6" stroke-width="2" stroke-linecap="round"/>
          <rect class="fill" x="7" y="12" width="4" height="2" rx="0.5" fill="#D6D6D6"/>
          <rect class="fill" x="7" y="16" width="4" height="2" rx="0.5" fill="#D6D6D6"/>
          <rect class="fill" x="13" y="12" width="4" height="2" rx="0.5" fill="#D6D6D6"/>
          <rect class="fill" x="13" y="16" width="4" height="2" rx="0.5" fill="#D6D6D6"/>
        </svg>
        <span class="text">Schedule</span>
      </RouterLink>
      
      <RouterLink class="menu-button" :class="{ active: isActiveRoute === '/shoppingcart' }" to="/shoppingcart">
        <svg class="icon" width="28" height="28" viewBox="0 0 28 28" fill="none" xmlns="http://www.w3.org/2000/svg">
          <path class="stroke" d="M4.66663 4.66663H6.60507C7.35502 4.66663 7.73 4.66663 8.00126 4.87842C8.27252 5.09022 8.36347 5.45399 8.54536 6.18155L8.76738 7.06963C8.94562 7.7826 9.03474 8.13909 9.21387 8.41695C9.45838 8.79624 9.82397 9.08168 10.2512 9.2269C10.5642 9.33329 10.9317 9.33329 11.6666 9.33329V9.33329" stroke="white" stroke-width="2" stroke-linecap="round"/>
          <path class="stroke" d="M21 19.8334H8.80939C8.43148 19.8334 8.24253 19.8334 8.10359 19.7922C7.66676 19.6629 7.37254 19.2547 7.388 18.7994C7.39292 18.6546 7.45267 18.4754 7.57218 18.1168V18.1168C7.70477 17.7191 7.77106 17.5202 7.86435 17.3541C8.15263 16.8407 8.65243 16.4805 9.23059 16.3693C9.41767 16.3334 9.62732 16.3334 10.0466 16.3334H16.3333" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
          <path class="stroke" d="M17.3612 16.3334H12.7218C11.1035 16.3334 10.2943 16.3334 9.7348 15.8594C9.17531 15.3855 9.04228 14.5873 8.77623 12.991L8.74883 12.8266C8.47857 11.205 8.34344 10.3942 8.79279 9.86381C9.24213 9.33337 10.0641 9.33337 11.708 9.33337H20.0972C21.5476 9.33337 22.2728 9.33337 22.5659 9.80764C22.859 10.2819 22.5347 10.9305 21.8861 12.2278L20.9389 14.1222C20.401 15.1981 20.132 15.736 19.6487 16.0347C19.1654 16.3334 18.564 16.3334 17.3612 16.3334Z" stroke="white" stroke-width="2" stroke-linecap="round"/>
          <circle class="fill" cx="19.8333" cy="23.3333" r="1.16667" fill="white"/>
          <circle class="fill" cx="10.5" cy="23.3333" r="1.16667" fill="white"/>
        </svg>
        <span class="text">Shopping Cart</span> 
      </RouterLink>
      <button id="logout" @click="handleLogout">
        Log out
      </button>
    </div>
  </aside>
</template>

<script setup>
// import the <RouterLink> component so that we can use it in the template above
import { RouterLink,useRoute } from "vue-router";
import { computed } from 'vue';
import { useAuth0 } from "@auth0/auth0-vue";
  
const { logout } = useAuth0();
// existing imports and code

const route = useRoute();
const isActiveRoute = computed(() => route.path);

const handleLogout = () => {
  logout({ 
    logoutParams: { 
      returnTo: window.location.origin 
    } 
  });
}


</script>

<style>
.menu {
  position: relative;
  height: 100%;
}

#logout {
  position: absolute;
  bottom: 0;
  width: 100%;
  height: 3rem;
  color: white;
  background-color: var(--auth0);
}

aside {
  display: flex;
  flex-direction: column;
  align-items: center;
  background-color: var(--primary-blue);
  width: var(--sidebar-width);
  overflow: hidden;
  padding: 0rem;
  padding-top: 2rem;

  /* Hide page elements if the y overlap the sidebar */
  @media (min-width: 768) {
    position: fixed;
    /* z-index: 99; */
  }
}

aside h1 {
  color: var(--sidebar-text-color);
  font-size: 25px;
  font-family: "Montserrat";
  font-weight: 700;
}

.title hr {
  height:2px;
  border-width:0;
  color:gray;
  background-color:gray;
  margin-top: 2rem;
  margin-bottom: 2rem;
}

.icon {
  margin-right: 0.5rem;
}

.menu {
  margin: 0 -1rem;
}

.menu-button {
  display: flex;
  align-items: center;
  text-decoration: none;
  padding: 0.5rem 3rem;
  border-radius: 0.05rem;
  
  .text {
    font-size: 15px;
    color: var(--sidebar-text-color);
    font-family: "Roboto";
    font-weight: 500;
  }

  &:hover {
    background-color: var(--sidebar-hover);

    .text {
      color: var(--primary-blue);
    }

    .icon .fill {
      fill: var(--primary-blue)
    }

    .icon .stroke {
      stroke: var(--primary-blue)
    }
  }
}

.menu-button.active {
  background-color: var(--sidebar-hover);
  /* filter: drop-shadow(0rem 0px 4px var(--accent-grey)); */

  .text {
    color: var(--primary-blue);
  }

  .icon .fill {
    fill: var(--primary-blue);
  }

  .icon .stroke {
    stroke: var(--primary-blue);
  }
}




/* give the header itself a background color, a border, and add some padding to the content */
/* .app-header {
  background-color: #fcfcfc;
  border-bottom: 1px solid #e0e0e0;
  padding: 1rem;
}

 make the title within the header a larger and bolder font 
.app-header h1 {
  font-size: 2rem;
  font-weight: bold;
} */

</style>


<!-- <header class="app-header">
  <div>
    <h1>{{ title }}</h1>
    <nav>
      <ul>
        <li>
          <RouterLink to="/">Home</RouterLink>
        </li>
        <li>
          <RouterLink to="/fetch">Fetch Example</RouterLink>
        </li>
        <li>
          <
            This RouterLink does not point to a specific path, but rather the name of a route.
            Check out router/index.js for how this is defined
          
          <RouterLink :to="{ name: 'form' }">Form Example</RouterLink>
        </li>
      </ul>
    </nav>
  </div>
</header> -->