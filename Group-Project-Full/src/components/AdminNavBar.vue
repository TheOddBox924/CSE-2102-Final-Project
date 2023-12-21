<template>
  <aside>
    <div class="title">
      <h1>Syllabus Sync</h1>
      <hr> 
    </div>
    <div class="menu">
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
    </div>
  </aside>
</template>

<script setup>
// import the <RouterLink> component so that we can use it in the template above
import { RouterLink,useRoute } from "vue-router";
import { computed } from 'vue';
// existing imports and code

const route = useRoute();
const isActiveRoute = computed(() => route.path);
// give this component a title property so that the parent component (app.vue) can set whatever title it wants
defineProps({
  title: {
    type: String,
    required: true,
  },
});
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