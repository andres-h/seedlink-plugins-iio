  <proc name="adxl500">
    <tree>
      <!-- Adjust according to actual sample rate -->
      <input name="X" channel="X" location="" rate="500"/>
      <input name="Y" channel="Y" location="" rate="500"/>
      <input name="Z" channel="Z" location="" rate="500"/>
      <node filter="FS2D5" stream="HN"/>
    </tree>
  </proc>
