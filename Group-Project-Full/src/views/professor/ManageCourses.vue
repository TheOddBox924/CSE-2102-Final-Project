<template>
  <!-- Teacher manage courses -->
  <!-- ok so basically, we could do list view or box view like huskyct. i like box view so we need a grid layout -->
  <main id="manage-courses">
    <div class="lds-dual-ring" v-show="activeCourses.length === 0"></div>
    <div id="active-grid">
        <div class="active-course" v-for="course in activeCourses">
            <div class="active-course-details">
              {{ course.cid }}
            </div>
            <div class="active-course-actions">
                <button class="drop-course-btn">

                </button>
            </div>
        </div>
    </div>
  </main>
</template>
<script setup>
import { ref, onMounted } from 'vue';
import { getUserCourses } from '@/util/apiCaller';
import { useAuth0 } from '@auth0/auth0-vue';
const { getAccessTokenSilently } = useAuth0();

// Define a reactive data property for courses
const activeCourses = ref([]);

onMounted(async () => {
  try {
    const accessToken = await getAccessTokenSilently();

    const courses = await getUserCourses('standard', accessToken);
    activeCourses.value = courses.data.items; // Update the reactive property with fetched data
    console.log(courses.data.items);
  } catch (error) {
    console.error("Failed to fetch courses:", error);
    // Handle error appropriately
  }
});
</script>


<style>

#manage-courses {
  position: relative;
}

#active-grid {
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 1rem;
}

.active-course {
    position: relative;
    width: 100%;
    height: 5rem;
    background: white;
    color: black;
    filter: drop-shadow(0rem 0px 2px var(--accent-grey));
    border-radius: 0.25rem;
    padding: 0.25rem;
}

/* make the heading font larger and add spacing below */
.manage h2 {
  font-size: 1.5rem;
  margin-bottom: 2rem;
}

.lds-dual-ring {
  display: inline-block;
  width: 80px;
  height: 80px;
  margin: auto;
  align-self: center;
}

.lds-dual-ring:after {
  content: " ";
  display: block;
  width: 64px;
  height: 64px;
  margin: 8px;  
  border-radius: 50%;
  border: 6px solid var(--primary-blue);
  border-color: var(--primary-blue) transparent var(--primary-blue) transparent;
  animation: lds-dual-ring 1.2s linear infinite;
}

@keyframes lds-dual-ring {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}
</style>