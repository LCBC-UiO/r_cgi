#!/usr/bin/env Rscript

# no support for special chars yet ("<" => "%3C")
params <- (function() {
  ret <- list()
  par <- unlist(strsplit(Sys.getenv("QUERY_STRING"), "[=&]"))
  if (length(par) == 0) return(ret)
  s <- seq(2, length(par), 2)
  ret[par[s-1]] <- par[s]
  return(ret)
})()


# send mime-type
cat(sprintf("Content-Type: image/png\r\n"))
# end of header
cat(sprintf("\r\n"))

png("/dev/stdout", width=as.numeric(params$width), height=as.numeric(params$height))
plot(1)
invisible(dev.off())
