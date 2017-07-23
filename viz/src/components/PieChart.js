import { Pie, mixins } from 'vue-chartjs';

const { reactiveProp } = mixins;

export default Pie.extend({
  mixins: [reactiveProp],
  props: ['options'],
  mounted() {
    this.renderChart(this.chartData, this.options);
  },
});
