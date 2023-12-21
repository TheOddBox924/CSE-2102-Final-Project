<template>
    <!-- Teacher manage courses -->
    <!-- ok so basically, we could do list view or box view like huskyct. i like box view so we need a grid layout -->
    <main class="t-manage-courses">
        <div id="active-grid">
            <div class="active-course" v-for="course in activeCourses">
                <div class="active-course-details">

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
import { ref } from 'vue';
import { useAuth0 } from '@auth0/auth0-vue';
const { getAccessTokenSilently } = useAuth0();

const activeCourses = ref(["Course 1", "Course 2"]);


</script>

<style>

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


</style>