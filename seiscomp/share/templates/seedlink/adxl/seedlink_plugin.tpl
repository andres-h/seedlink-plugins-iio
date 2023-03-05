* template: $template
plugin $seedlink.source.id cmd = "$seedlink.plugin_dir/iio_accel_plugin -d $sources.adxl.device -r $sources.adxl.sampleRate -s $seedlink.station.id"
             timeout = 600
             start_retry = 60
             shutdown_wait = 10
             proc = "$sources.adxl.proc"

