* template: $template
plugin $seedlink.source.id cmd = "$seedlink.plugin_dir/w1_humid_plugin -d $sources.w1humid.device -r $sources.w1humid.sampleRate -s $seedlink.station.id"
             timeout = 600
             start_retry = 60
             shutdown_wait = 10
             proc = "$sources.w1humid.proc"

