<template>
  <div class="type-distribution">
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
        labels: ['攻击', '防御', '生命', '暴击', '速度', '攻击加成', '防御加成', '生命加成', '暴击伤害', '效果命中', '效果抵抗'],
        datasets: [
          {
            label: 'GitHub Commits',
            backgroundColor: ['hsla(24%, 100%, 71%, 1)', 'hsla(49%, 100%, 72%, 1)', 'hsla(59%, 100%, 74%, 1)', 'hsla(197%, 80%, 65%, 1)', 'hsla(238%, 70%, 73%, 1)', 'hsla(24%, 100%, 55%, 1)', 'hsla(49%, 100%, 56%, 1)', 'hsla(59%, 100%, 60%, 1)', 'hsla(198%, 100%, 45%, 1)', 'hsla(238%, 70%, 57%, 1)', 'hsla(284%, 70%, 57%, 1)'],
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
