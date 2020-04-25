#!/usr/bin/env Rscript

# send mime-type
cat(sprintf("Content-Type: image/png\r\n"))
# end of header
cat(sprintf("\r\n"))

png("/dev/stdout")
plot(1)
invisible(dev.off())
