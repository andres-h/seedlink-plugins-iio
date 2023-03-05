* template: $template
plugin $seedlink.source.id cmd = "$seedlink.plugin_dir/iio_baro_plugin -d $sources.dps.device -r $sources.dps.sampleRate -s $seedlink.station.id"
             timeout = 600
             start_retry = 60
             shutdown_wait = 10
             proc = "$sources.dps.proc"

