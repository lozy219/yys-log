import { PolarArea, mixins } from 'vue-chartjs';

const { reactiveProp } = mixins;

export default PolarArea.extend({
  mixins: [reactiveProp],
  props: ['options'],
  mounted() {
    this.renderChart(this.chartData, this.options);
  },
});
