<template>
  <section class="section">
    <div class="container">
      <div class="columns">
        <div class="column is-three-quarters content">
          <h1><i class="fas fa-arrow-circle-right"></i> 开始玩东方符斗祭之前你需要知道的事</h1>
          <ol>
            <li>东方符斗祭（aka. THB，THBattle，以下简称 THB）游戏本体免费，未来也不会出现影响游戏平衡的收费项目。</li>
            <li>THB 会不定期出一些周边产品，如果可以的话还请多支持。</li>
            <li>THB 在目前所有流行的平台上都有客户端，包括 Windows/macOS/Linux/Android/iOS</li>
          </ol>
          <hr>
          <h1><i class="fas fa-arrow-circle-right"></i> 关于社区氛围的说明</h1>
          <ol>
            <li>THB 一直以来都是一个小社区，玩家们在这里交朋友的有很多，社区氛围一直良好。</li>
            <li>这里没有一个明确可以遵守的守则，但是有一个原则：请不要把你的恶意泼洒在这里，请小心维护有爱的社区氛围。</li>
            <li>因为是免费游戏，黑幕组对破坏社区氛围的行为绝不会手软，阈值很低处罚严厉。</li>
            <li>常见的破坏社区氛围的行为：辱骂、恶意游戏（鞭尸、不按身份出牌、挂机）。</li>
          </ol>
          <hr>
          <h1><i class="fas fa-arrow-circle-right"></i> 关于注册和绑定论坛帐号的说明</h1>
          <ol>
            <li>注册需要手机号，一个手机号只能注册一个帐号。</li>
            <li>游戏中的昵称不可以与其他人重复，不可以是常见人物名称（如“风见幽香”）。</li>
            <li>老用户绑定论坛帐号后，论坛的 id 、名称以及之前的节操、游戏数、掉线数、勋章会保留。</li>
            <li>绑定论坛帐号只能进行一次，不可逆。</li>
            <li>一个论坛帐号只能绑定一个游戏帐号。</li>
          </ol>
        </div>
        <div class="column">
          <div class="field">
            <label class="label">手机</label>
            <div class="control">
              <input class="input" type="text" placeholder="Text input">
            </div>
          </div>

          <div class="field">
            <label class="label">密码</label>
            <div class="control has-icons-left has-icons-right">
              <input class="input is-success" type="text" placeholder="Text input" value="bulma">
              <span class="icon is-small is-left">
                <i class="fas fa-user"></i>
              </span>
              <span class="icon is-small is-right">
                <i class="fas fa-check"></i>
              </span>
            </div>
            <p class="help is-success">This username is available</p>
          </div>

          <div class="field">
            <label class="label">游戏昵称</label>
            <div class="control has-icons-left has-icons-right">
              <input class="input is-danger" type="email" placeholder="Email input" value="hello@">
              <span class="icon is-small is-left">
                <i class="fas fa-envelope"></i>
              </span>
              <span class="icon is-small is-right">
                <i class="fas fa-exclamation-triangle"></i>
              </span>
            </div>
            <p class="help is-danger">This email is invalid</p>
          </div>

          <div class="field">
            <label class="label">Subject</label>
            <div class="control">
              <div class="select">
                <select>
                  <option>Select dropdown</option>
                  <option>With options</option>
                </select>
              </div>
            </div>
          </div>

          <div class="field">
            <label class="label">Message</label>
            <div class="control">
              <textarea class="textarea" placeholder="Textarea"></textarea>
            </div>
          </div>

          <div class="field">
            <div class="control">
              <label class="checkbox">
                <input type="checkbox">
                I agree to the <a href="#">terms and conditions</a>
              </label>
            </div>
          </div>

          <div class="field">
            <div class="control">
              <label class="radio">
                <input type="radio" name="question">
                Yes
              </label>
              <label class="radio">
                <input type="radio" name="question">
                No
              </label>
            </div>
          </div>

          <div class="field is-grouped">
            <div class="control">
              <button class="button is-link">Submit</button>
            </div>
            <div class="control">
              <button class="button is-text">Cancel</button>
            </div>
          </div>
        </div>
        </div>
      </div>
  </section>
</template>
<!--
<style lang="sass">
</style>
-->
<script>
export default {
  name: 'Login',
}
</script>
