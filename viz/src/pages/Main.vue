<template>
  <div class="main">
    <div class="side-panel">
      <img v-for="img in imgPath" class="side-logo" :src="require(`../assets/img/${img}`)">
    </div>
    <div class="stats-panel">
      <star-distribution :counts="starCounts">
      </star-distribution>
    </div>
  </div>
</template>

<script>
import StarDistribution from '@/components/StarDistribution';

export default {
  name: 'main',
  components: {
    'star-distribution': StarDistribution,
  },
  data() {
    return {
      imgPath: ['三味.png', '火灵.png', '钟灵.png', '伤魂鸟.png', '狰.png', '铃女.png', '反枕.png', '珍珠.png', '镇墓兽.png', '地藏像.png', '破势.png', '镜姬.png', '天邪.png', '网切.png', '阴魔罗.png', '小袖之手.png', '薙魂.png', '雪幽魂.png', '心眼.png', '蚌精.png', '青鹭火.png', '招财猫.png', '蝠翼.png', '骰子鬼.png', '日女巳时.png', '被服.png', '魅妖.png', '木魅.png', '轮入道.png', '魍魉之匣.png', '树妖.png', '返魂香.png', '鸣屋.png', '涅槃之火.png', '针女.png'],
    };
  },
  computed: {
    counts() {
      return {
        five: 18,
        six: 4,
      };
    },
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
@import '../styles/constants.scss';

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

    img {
      transition: all 0.4s ease-in-out;
      width: 100px;
      cursor: pointer;
      filter: grayscale(100%);

      &:hover {
        filter: none;
      }
    }
  }
  .stats-panel {
    margin-left: $side-panel-width;
  }
}
</style>
