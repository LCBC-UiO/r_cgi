#!/usr/bin/env Rscript

params <- (function() {
  ret <- list()
  par <- unlist(strsplit(Sys.getenv("QUERY_STRING"), "[=&]"))
  if (length(par) == 0) return(ret)
  s <- seq(2, length(par), 2)
  ret[par[s-1]] <- par[s]
  return(ret)
})()

# handle any special characters in string
# https://www.w3schools.com/jsref/jsref_decodeuricomponent.asp
decodeURIComponent <- function(str) {
  chars <- unlist(strsplit(str,""))
  out <- c()
  i <- 1
  while (i <= length(chars)) {
    if(chars[i] == "%") {
      n <- rawToChar(as.raw(sprintf("0x%s%s", chars[i+1], chars[i+2])))
      out <- c(out, n)
      i = i+3
      next()
    }
    out <- c(out, chars[i])
    i <- i+1
  }
  return(paste0(out,collapse=""))
}
params$title <- decodeURIComponent(params$title)

# send mime-type
cat(sprintf("Content-Type: image/png\r\n"))
# end of header
cat(sprintf("\r\n"))

# plot

png("/dev/stdout", width=as.numeric(params$width), height=as.numeric(params$height))
plot(1, main=params$title)
if (params$showLegend == 1) {
  legend("topleft","test", fill="red")
}
invisible(dev.off())
