<template>
  <main id="search">
    <!-- <h2>Search Courses</h2> -->

    <div id="search-bar">
      <svg width="20" height="20" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg">
        <path fill-rule="evenodd" clip-rule="evenodd"
          d="M6.00001 0C6.55229 0 7.00001 0.447715 7.00001 1L7.00001 3H13V1C13 0.447715 13.4477 0 14 0C14.5523 0 15 0.447715 15 1V3L15.0658 3C15.9523 2.99995 16.7161 2.99991 17.3278 3.08214C17.9833 3.17027 18.6117 3.36902 19.1213 3.87868C19.631 4.38834 19.8297 5.01669 19.9179 5.67221C20.0001 6.28387 20.0001 7.0477 20 7.93419L20 8V15L20 15.0658C20.0001 15.9523 20.0001 16.7161 19.9179 17.3278C19.8297 17.9833 19.631 18.6117 19.1213 19.1213C18.6117 19.631 17.9833 19.8297 17.3278 19.9179C16.7161 20.0001 15.9523 20.0001 15.0658 20L15 20H5.00001L4.9342 20C4.0477 20.0001 3.28388 20.0001 2.67221 19.9179C2.0167 19.8297 1.38835 19.631 0.878686 19.1213C0.369024 18.6117 0.170279 17.9833 0.0821467 17.3278C-8.88109e-05 16.7161 -4.60148e-05 15.9523 3.8147e-06 15.0658L6.19888e-06 15V8L3.8147e-06 7.93417C-4.60148e-05 7.04768 -8.88109e-05 6.28387 0.0821467 5.67221C0.170279 5.01669 0.369024 4.38834 0.878686 3.87868C1.38835 3.36902 2.0167 3.17027 2.67221 3.08214C3.28388 2.99991 4.04769 2.99995 4.93418 3L5.00001 3V1C5.00001 0.447715 5.44772 0 6.00001 0ZM13 5C13 5.55228 13.4477 6 14 6C14.5523 6 15 5.55228 15 5C15.9711 5 16.5988 5.00212 17.0613 5.06431C17.495 5.12262 17.631 5.21677 17.7071 5.29289C17.7832 5.36902 17.8774 5.50496 17.9357 5.9387C17.9979 6.40121 18 7.02892 18 8H2.00001C2.00001 7.02892 2.00213 6.40121 2.06431 5.9387C2.12263 5.50496 2.21678 5.36902 2.2929 5.29289C2.36902 5.21677 2.50497 5.12262 2.93871 5.06431C3.40122 5.00212 4.02893 5 5.00001 5C5.00001 5.55228 5.44772 6 6.00001 6C6.55229 6 7.00001 5.55228 7.00001 5H13ZM2.00001 15V10H18V15C18 15.9711 17.9979 16.5988 17.9357 17.0613C17.8774 17.495 17.7832 17.631 17.7071 17.7071C17.631 17.7832 17.495 17.8774 17.0613 17.9357C16.5988 17.9979 15.9711 18 15 18H5.00001C4.02893 18 3.40122 17.9979 2.93871 17.9357C2.50497 17.8774 2.36902 17.7832 2.2929 17.7071C2.21678 17.631 2.12263 17.495 2.06431 17.0613C2.00213 16.5988 2.00001 15.9711 2.00001 15ZM7.00001 13C6.44772 13 6.00001 13.4477 6.00001 14C6.00001 14.5523 6.44772 15 7.00001 15H13C13.5523 15 14 14.5523 14 14C14 13.4477 13.5523 13 13 13H7.00001Z"
          fill="var(--accent-grey)" />
      </svg>

      <select id="period" name="period">
        <option value="Fall 2023">Fall 2023</option>
        <option value="Spring 2024">Spring 2024</option>
        <option value="Fall 2024">Fall 2024</option>
        <option value="Spring 2025">Spring 2025</option>
      </select>

      <div id="input-wrapper">
        <input id="search-input" 
            ref="searchInput"
            type="text" 
            placeholder="Search Courses, Professors, Locations..." 
            v-model="query"
            v-on:keyup.enter="performSearch"
            @focus="searchHistoryVisible = true" 
            @blur="searchHistoryVisible = false">
        <div id="search-preview" v-if="searchHistory.length > 0 && query.length != 0 && searchHistoryVisible">
          <div class="sp-wrapper" v-for="query in searchHistory">
            {{ query }}
          </div>
        </div>
      </div>
      
      <div id="filters">
        <button id="filters-button" @click="toggleFilterDropdown" v-on-click-outside="hideFilterDropdown">
          <svg width="18" height="16" viewBox="0 0 18 16" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path fill-rule="evenodd" clip-rule="evenodd"
              d="M8 3C8 2.44772 7.55228 2 7 2C6.44772 2 6 2.44772 6 3C6 3.55228 6.44772 4 7 4C7.55228 4 8 3.55228 8 3ZM17 4L9.82929 4C9.41746 5.16519 8.30622 6 7 6C5.69378 6 4.58254 5.16519 4.17071 4L1 4C0.447715 4 0 3.55228 0 3C0 2.44772 0.447715 2 1 2L4.17071 2C4.58254 0.834807 5.69378 0 7 0C8.30622 0 9.41746 0.834808 9.82929 2L17 2C17.5523 2 18 2.44772 18 3C18 3.55228 17.5523 4 17 4ZM14.8293 12C14.4175 10.8348 13.3062 10 12 10C10.6887 10 9.57385 10.8414 9.1659 12.0137C9.11194 12.0047 9.05652 12 9 12L1 12C0.447715 12 0 12.4477 0 13C0 13.5523 0.447715 14 1 14L9 14C9.05652 14 9.11194 13.9953 9.1659 13.9863C9.57385 15.1586 10.6887 16 12 16C13.3062 16 14.4175 15.1652 14.8293 14H17C17.5523 14 18 13.5523 18 13C18 12.4477 17.5523 12 17 12H14.8293ZM13 13C13 12.4477 12.5523 12 12 12C11.4477 12 11 12.4477 11 13C11 13.5523 11.4477 14 12 14C12.5523 14 13 13.5523 13 13Z"
              fill="#12263A" />
          </svg>
          Filters
        </button>
        <div v-if="dropdownVisible" class="filter-dropdown ignore-click-outside">
          <details class="filter-category" v-for="category in filterCategories" :key="category.name">
            <summary><strong>{{ category.name }}</strong></summary>
            <li v-for="option in category.options" :key="option">
              <input type="checkbox" :value="option" :checked="isFilterChecked(option)" @change="updateFilters(option)">
              {{ option }}
            </li>
          </details>
        </div>
      </div>

      <button id="search-button" @click="performSearch">
        Search
      </button>
    </div>

    <div id="search-results">
      <RouterLink class="search-result" :to="{ name: 'courseinfo', query: { cid: result.cid, title: result.title, desc: result.description, creditHours: result.creditHours, preReqs: result.prereqs }}" v-for="result in searchResults">
        <div class="result-item">
          <b>{{ result.cid }}</b>&nbsp;{{ result.title }}
        </div>
        <div class="result-item-details">
          {{ result.creditHours }} Credits
        </div>
        <div class="result-item-details">
          {{ result.openSections }} Openings
        </div>
      </RouterLink>
    </div>
  </main>
</template>

<script setup>
import { ref } from 'vue';
import { useAuth0 } from '@auth0/auth0-vue';
import { searchCourses } from '@/util/apiCaller';
const { getAccessTokenSilently } = useAuth0();


const dropdownVisible = ref(false);
const selectedFilters = ref([]);
const filterCategories = ref([
  { name: 'Content Area', options: ['CA1', 'CA2', 'CA3', 'CA4'] },
  { name: 'Requirement', options: ['E Course', 'W Course'] },
  { name: 'Availability', options: ['Available', 'Waitlisted', 'Full'] },
  { name: 'Rating', options: ['5'] }
]);

const toggleFilterDropdown = () => dropdownVisible.value = !dropdownVisible.value;
const hideFilterDropdown = () => dropdownVisible.value = false;
const isFilterChecked = (option) => selectedFilters.value.includes(option);

const updateFilters = (option) => {
  if (selectedFilters.value.includes(option)) {
    const index = selectedFilters.value.indexOf(option);
    selectedFilters.value.splice(index, 1);
  } else {
    selectedFilters.value.push(option);
  }
}

// ====================== Search Results
const searchInput = ref();
const searchResults = ref([]);
const searchHistory = ref([]);
const searchHistoryVisible = ref();
const query = ref(''); // Binds to the v-model 'query' in the input tag

const performSearch = async () => {
  searchResults.value = [];
  console.log('performing search');
  console.log(`Fetching search data: ${query.value}`);

  const accessToken = await getAccessTokenSilently();
  const results = await searchCourses(query.value, accessToken);
  searchResults.value = results.data;
}

defineExpose({ hideFilterDropdown })
</script>

<style>
hr {
  height: 0.15rem;
  border-width: 0;
  color: var(--accent-grey);
  background-color: var(--accent-grey);
  width: 100%;
  margin-bottom: 1rem;
  margin-top: 2rem;
}

#search {
  position: relative;
  text-align: center;
  align-items: center;
}

/* make the heading font larger and add spacing below */
#search h2 {
  font-size: 2.5rem;
  margin-bottom: 2rem;
  font-family: "Montserrat";
  font-weight: 400;
}

#search-bar {
  height: 4rem;
  display: flex;
  align-items: center;
  position: relative;
  margin: auto;
  margin-bottom: 1rem;
  width: 100%;
  padding: 1rem;
  padding-right: 0rem;
  background-color: #FFFFFF;
  filter: drop-shadow(0rem 0px 10px var(--accent-grey));
  /* border: var(--sidebar) 2px solid */
  border-radius: 0.25rem;

}

input::placeholder {
  color: var(--accent-grey);
}

#input-wrapper {
  position: relative;  /* set the position to relative */
  flex-grow: 1;  /* this will make it as wide as search-input */
}

#search-input {
  height: 3rem;
  width: 100%;
  padding-left: 1rem;
  border-radius: 0.25rem;
}

#search-input:focus {
  outline: none;
}

#search-preview {
  position: absolute;
  top: 150%;
  width: 100%;
  z-index: 1;
  display: flex;
  flex-direction: column;
  max-height: 30rem;
  border: none;
  overflow-y: scroll;
  margin-top: -1rem;
  padding: 1rem;
  gap:0.5rem;
  filter: drop-shadow(0rem 10px 5px var(--accent-grey));
  background-color: #FFFFFF;
  /* border-radius: 1rem; */
}

.sp-wrapper {
  align-self: flex-start;
}

.search-results {
  max-height: 100%;
  /* Adjust SOME_OFFSET as needed */
  overflow-y: auto;
}

.search-result {
  display: flex;
  flex-direction: column;
  justify-content: center;  /* Vertical centering */
  margin-bottom: 1rem;
  background-color: #FFFFFF;
  border-radius: 0.25rem;
  padding: 1rem;
}

.result-item{
  align-self: flex-start;  /* Horizontal alignment to the left */
  margin-bottom: 1rem;
}

.result-item-details {
  align-self: flex-start;
  margin: 0.25rem
}


.search-result:hover {
  background-color: #dbdbdb;
}


#filters {
  position: relative;
  display: flex;
  flex-direction: column;
  width: 7%;
}

#filters-button {
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
  background: white;
  color: var(--sidebar);
  border: var(--sidebar) solid 2px;
  height: 2.5rem;
  width: 100%;
  margin-left: 0rem;

  svg {
    margin-right: 0.5rem;
  }
}

.filter-dropdown {
  position: absolute;
  display: flex;
  flex-direction: column;
  top: 150%;
  /*place it right below the parent element*/
  width: 10rem;
  /* take full width of parent */
  /* z-index: 1;          to make it appear above other elements */
  background-color: white;
  z-index: 99;
}

.filter-category {
  position: relative;
  padding: auto;

  li {
    text-align: left;
    list-style: none;
    margin-left: 2rem;
    margin-bottom: 0.5rem;
    padding: 0;
  }

  summary {
    padding-left: 2rem;
    cursor: default;
    /* prevents different cursor style */
    height: 3rem;
    display: flex;
    align-items: center;
    /* This will vertically center the text */
    justify-content: left;
  }

  summary:hover {
    background-color: #dbdbdb;
  }

  input[type='checkbox'] {
    margin-right: 0.5rem;
    /* Double-sized Checkboxes */
    -ms-transform: scale(1.25);
    /* IE */
    -moz-transform: scale(1.25);
    /* FF */
    -webkit-transform: scale(1.25);
    /* Safari and Chrome */
    -o-transform: scale(1.25);
    /* Opera */
    transform: scale(1.25);
    accent-color: var(--accent-orange);

  }
}

#search-button {
  background: var(--accent-b-orange);
  color: black;
  /* border-radius: 1rem; */
  height: 4rem;
  width: 10%;
  margin-left: 1rem;
  font-weight: 600;
  border-radius: 0 0.25rem 0.25rem 0rem;
}

#search-button:hover {
  background: var(--accent-b-orange-hover);
}

select {
  background: white;
  height: 100%;
  color: var(--accent-grey);
  border-radius: 1rem;
  margin-left: 1rem;
  font-weight: 500;
}</style>