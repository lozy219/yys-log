<template>
  <div class="main">
    <div class="background">
    </div>
    <div class="side-panel" id="side-panel">
      <img
        v-for="mitama in mitamas"
        class="side-logo"
        :class="{ 'side-logo-active': selected === mitama }"
        :src="require(`../assets/img/${mitama}.png`)"
        @click="mitamaSelect(mitama, $event)"
      >
    </div>
    <div class="stats-panel">
      <div class="semi-pseudo-panel" :style="panelStyle[0]">
      </div>
      <div class="semi-pseudo-panel" :style="panelStyle[1]">
      </div>
      <div class="stats-column">
        <star-distribution :counts="starCounts">
        </star-distribution>
      </div>
      <div class="stats-column">
        <position-distribution :counts="positionCounts">
        </position-distribution>
      </div>
      <div class="stats-column">
        <type-distribution :counts="typeCounts">
        </type-distribution>
      </div>
    </div>
  </div>
</template>

<script>
import Vue from 'vue';
import Vibrant from 'node-vibrant';
import StarDistribution from '@/components/StarDistribution';
import PositionDistribution from '@/components/PositionDistribution';
import TypeDistribution from '@/components/TypeDistribution';

const metadata = require('@/assets/data.json');

export default {
  name: 'main',
  components: {
    'star-distribution': StarDistribution,
    'position-distribution': PositionDistribution,
    'type-distribution': TypeDistribution,
  },
  data() {
    return {
      mitamas: ['三味', '火灵', '钟灵', '伤魂鸟', '狰', '铃女', '反枕', '珍珠', '镇墓兽', '地藏像', '破势', '镜姬', '天邪', '网切', '阴摩罗', '小袖之手', '薙魂', '雪幽魂', '心眼', '蚌精', '青鹭火', '招财猫', '蝠翼', '骰子鬼', '日女巳时', '被服', '魅妖', '木魅', '轮入道', '魍魉之匣', '树妖', '返魂香', '鸣屋', '涅槃之火', '针女'],
      selected: false,
      deferredSelected: false,
      styleFactors: [
        {
          rotateDeg: 135,
          dark: [0, 0, 0],
          light: [50, 50, 50],
        },
        {
          rotateDeg: 135,
          dark: [0, 0, 0],
          light: [50, 50, 50],
        },
      ],
      flipCount: 0,
    };
  },
  computed: {
    wrap() {
      if (this.selected) {
        return metadata[this.selected];
      }
      return metadata;
    },
    starCounts() {
      if (!this.wrap) {
        return [0, 0];
      }
      return [this.wrap['五星'], this.wrap['六星']];
    },
    positionCounts() {
      if (!this.wrap) {
        return [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0];
      }
      return [this.wrap['一号位'], this.wrap['二号位'], this.wrap['三号位'], this.wrap['四号位'], this.wrap['五号位'], this.wrap['六号位']];
    },
    typeCounts() {
      if (!this.wrap) {
        return [10, 0, 0, 0, 0, 0];
      }
      return [this.wrap['攻击'], this.wrap['防御'], this.wrap['生命'], this.wrap['暴击'], this.wrap['速度'], this.wrap['攻击加成'], this.wrap['防御加成'], this.wrap['生命加成'], this.wrap['暴击伤害'], this.wrap['效果命中'], this.wrap['效果抵抗']];
    },
    panelStyle() {
      const factors1 = this.styleFactors[0];
      const dark1 = factors1.dark;
      const light1 = factors1.light;
      const factors2 = this.styleFactors[1];
      const dark2 = factors2.dark;
      const light2 = factors2.light;
      const f = this.flipCount;
      return [
        `background-image: linear-gradient(${factors1.rotateDeg}deg, rgba(${dark1[0]}, ${dark1[1]}, ${dark1[2]}, 0.55), rgba(${light1[0]}, ${light1[1]}, ${light1[2]}, 0.55)); opacity: ${1 - f}`,
        `background-image: linear-gradient(${factors2.rotateDeg}deg, rgba(${dark2[0]}, ${dark2[1]}, ${dark2[2]}, 0.55), rgba(${light2[0]}, ${light2[1]}, ${light2[2]}, 0.55)); opacity: ${f}`,
      ];
    },
  },
  methods: {
    setStyleFactor(dark, light) {
      this.flipCount = 1 - this.flipCount;
      /* eslint no-bitwise: ["error", { "allow": ["~"] }] */
      this.styleFactors[this.flipCount].rotateDeg = ~~(Math.random() * 360);
      this.styleFactors[this.flipCount].dark = dark;
      this.styleFactors[this.flipCount].light = light;
    },
    mitamaSelect(name, $event) {
      this.selected = this.selected !== name && name;
      if (this.selected) {
        const vibrant = new Vibrant($event.target);
        vibrant.getPalette().then((palette) => {
          const { DarkVibrant, LightVibrant } = palette;
          const dark = DarkVibrant.getRgb();
          const light = LightVibrant.getRgb();
          this.setStyleFactor(dark, light);
        });
      } else {
        this.setStyleFactor([0, 0, 0], [50, 50, 50]);
      }
      Vue.nextTick(() => {
        setTimeout(() => {
          this.deferredSelected = this.selected;
        }, 200);
      });
    },
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
@import '../styles/constants.scss';

.background {
  background: rgb(53, 73, 94);
  width: 100vw;
  height: 100vh;
  position: fixed;
  top: 0;
  left: 0;
  z-index: -1;
}

.main {
  .side-panel {
    position: fixed;
    height: 100vh;
    width: $side-panel-width;
    top: 0px;
    left: 0px;
    overflow: scroll;
    color: white;
    display: flex;
    flex-direction: column;
    align-items: center;

    .side-logo {
      transition: all 0.4s ease-in-out;
      width: 100px;
      cursor: pointer;
      filter: grayscale(100%);

      &:hover {
        filter: grayscale(60%);
      }

      &.side-logo-active {
        filter: none;
      }
    }
  }

  .stats-panel {
    margin: $stats-panel-margin;
    margin-left: $side-panel-width;
    padding: $stats-panel-margin;
    position: relative;
    display: flex;
    border-radius: 40px;
    height: calc(100vh - 4 * #{$stats-panel-margin});
    box-shadow: 6px 5px 13px 1px rgba(0, 0, 0, 0.45);

    .semi-pseudo-panel {
      position: absolute;
      top: 0;
      left: 0;
      right: 0;
      bottom: 0;
      transition: all ease-in-out 0.6s;
      border-radius: inherit;
      z-index: -1;
    }
  }

  .stats-column {
    flex: 1;
    display: flex;
    justify-content: center;
    align-items: center;
    height: inherit;
  }
}
</style>
