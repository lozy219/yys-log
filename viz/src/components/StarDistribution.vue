<template>
  <div class="star-distribution">
    <pie-chart :chart-data="charData" :width="300" :height="400" :options="options">
    </pie-chart>
  </div>
</template>

<script>
import PieChart from '@/components/PieChart';

export default {
  props: ['counts'],
  components: {
    'pie-chart': PieChart,
  },
  computed: {
    charData() {
      return {
        labels: ['五星御魂', '六星御魂'],
        datasets: [
          {
            label: 'GitHub Commits',
            backgroundColor: ['#FFE2AD', '#E89685'],
            data: this.counts,
          },
        ],
      };
    },
    options() {
      return {
        responsive: false,
        maintainAspectRatio: false,
        legend: {
          position: 'bottom',
          fullWidth: true,
          labels: {
            fontColor: '#fff',
          },
        },
      };
    },
  },
};
</script>

<style lang="scss" scoped>

</style>
