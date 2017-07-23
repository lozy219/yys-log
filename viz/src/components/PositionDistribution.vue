<template>
  <div class="position-distribution">
    <polar-chart :chart-data="charData" :width="700" :height="600" :options="options">
    </polar-chart>
  </div>
</template>

<script>
import PolarChart from '@/components/PolarChart';

export default {
  props: ['counts'],
  components: {
    'polar-chart': PolarChart,
  },
  computed: {
    charData() {
      return {
        labels: ['一号位', '二号位', '三号位', '四号位', '五号位', '六号位'].reverse(),
        datasets: [
          {
            label: 'GitHub Commits',
            backgroundColor: ['#037EF3', '#F85A40', '#F48924', '#C15EFF', '#FFC845', '#7EEFBE'].reverse(),
            data: this.counts,
          },
        ],
      };
    },
    options() {
      return {
        responsive: false,
        maintainAspectRatio: false,
        scale: {
          display: false,
        },
        startAngle: -0.5 * Math.PI,
        legend: {
          reverse: true,
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
