<template>
  <main class="schedule">
    <div id="schedule-headers">
        <div v-for="day in days">
          {{ day }}
        </div>
      </div>
    <div id="schedule-layout">
      <div id="schedule-times">
        <div class="time-segment" v-for="segment in time_segments" :key="segment">
          {{ segment }}
        </div>
      </div>
      <div class="day-grid-layout" v-for="(day, dayIndex) in days" :key="dayIndex">
        <div class="day-segment" v-for="segment in segments">
        </div>
        <div class="day-event" v-if="activeEvents[dayIndex] && activeEvents[dayIndex].length > 0" v-for="event in activeEvents[dayIndex] || []" :style="getEventStyle(event)">
            <p class="event-header">{{ event.cid }} - {{ event.title }}</p>
            <p class="event-time">{{ convertToStandardTime(event.startTime) }} - {{ convertToStandardTime(event.endTime) }}</p>
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
const activeEvents = ref([]);

onMounted(async () => {
  try {
    const accessToken = await getAccessTokenSilently();

    const events = await getUserCourses('schedule', accessToken);
    activeEvents.value = events.data.items; // Update the reactive property with fetched data
    console.log(activeEvents);
  } catch (error) {
    console.error("Failed to fetch courses:", error);
  }
});

const segments = ref(24);
const segment_height_rem = 3;
const time_segments = ref([
  "1 AM", "2 AM", "3 AM", "4 AM", "5 AM",
  "6 AM", "7 AM", "8 AM", "9 AM", "10 AM",
  "11 AM", "12 PM", "1 PM", "2 PM", "3 PM",
  "4 PM", "5 PM", "6 PM", "7 PM", "8 PM",
  "9 PM", "10 PM", "11 PM", "12 AM"
]);
const days = ref([
  "Sunday",
  "Monday",
  "Tuesday",
  "Wednesday",
  "Thursday",
  "Friday",
  "Saturday"
])

const convertToStandardTime = (time) => {
  let [hours, minutes] = time.split(':').map(Number);
  let period = hours >= 12 ? 'PM' : 'AM';
  hours = hours % 12 || 12; // Convert "0" hour to "12"

  let s_mins = ""
  if (minutes === 0) {
    s_mins = "00";
  } else {
    s_mins = minutes.toString();
  }
  return `${hours}:${s_mins} ${period}`;
}

const timeToPosition = (startTime) => {
  var top_px = 0;

  const [hours, minutes] = startTime.split(":").map(Number);

  top_px += (hours * (16 * segment_height_rem)); // 16 * 3 because the height of one segment is 3 rem (1 rem = 16px)
  top_px += ((minutes / 60) * (16 * segment_height_rem)) // Convert minutes to percentage and multiply by height of segment in pixels
  console.log(`start ${startTime}`);
  console.log(`hours mins ${hours}, ${minutes}`);
  console.log(`top ${top_px}`);
  return top_px;
}

const durationToHeight = (startTime, endTime) => {
  var height_px = 0

  const [s_hours, s_minutes] = startTime.split(":").map(Number); // Start times
  const [e_hours, e_minutes] = endTime.split(":").map(Number); // End times

  const d_hours = e_hours - s_hours // Total event duration hours
  const d_minutes = e_minutes - s_minutes // Total event duration minutes
  
  const duration = ((d_hours * (16 * segment_height_rem)) + ((d_minutes / 60) * (16 * segment_height_rem)));

  if (duration < 24) {
    var height_px = 24; // Set a default height for no duration
  }
  // See timeToPosition for more details on how this calculation works
  height_px = duration;
  console.log(height_px);
  return height_px;
}

const getEventStyle = (event) => {
  // Logic to convert start and end times to rem values.
  // Changes the top and height attributes of the event
  const top = timeToPosition(event.startTime);
  const height = durationToHeight(event.startTime, event.endTime);

  return {
    position: 'absolute',
    top: `${top}px`, // Or `${top}%` if using percentage
    height: `${height}px`
    // More styles here
  };
};


</script>

<style>

#schedule-layout {
  display: flex;
  max-height: 99%;
  overflow-y: auto;
}

#schedule-headers {
  display: flex;  
  flex-grow: 1;
  margin-left: 3rem;
  font-size: 15px;
  font-weight: 300;
  color: var(--accent-grey);
  box-shadow: 0 3px 5px -5px rgb(54, 54, 54);
}

#schedule-headers > div {
  flex: 1 0 0;
  align-items: center;
  justify-content: center;
  text-align: center;
}

.day-grid-layout {
  position: relative;
  display: flex;
  flex-direction: column;
  flex-grow: 1;
}

.time-segment {
  margin-right: 0.5rem;
  padding-top: 2.1rem;
  height: 3rem;
  min-width: 3rem;
  color: var(--accent-grey);
  font-size: 15px;
}

.day-segment {
  padding: 1rem;
  width: 100%;
  min-height: 3rem;
  border-bottom: 1px solid var(--accent-grey);
  border-right: 1px solid var(--accent-grey);
  display: flex; /* Use flexbox for centering */
  align-items: center; /* Center vertically */
  justify-content: center; /* Center horizontally */
  text-align: center; /* Ensures that the text is centered if it wraps onto multiple lines */
}

.day-event {
  position: absolute;
  width: 98%;
  background: var(--studentadmin-green);
  border-radius: 0.25rem;
  padding: 0.5rem;
  transition: all 0.3s ease;
}

.day-event > p {
  color: black;
  font-size: 13px;
  font-weight: 500;
}

.day-event:hover {
  /* transform: translate(-5px, -5px); */
  filter: drop-shadow(0px 0px 5px var(--accent-grey));
}

</style>