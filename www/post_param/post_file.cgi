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
params$filename <- decodeURIComponent(params$filename)

# read everything from stdin
d <- read.table(file("stdin"), sep=",")

# write to a new file
write.table(d, file=params$filename)

# send header

# tell client that everything went fine
cat(sprintf("Status: 200\r\n"))
# what are we sending back?
cat(sprintf("Content-type: application/json\r\n"))
# end of header
cat(sprintf("\r\n"))

# send body

cat(sprintf('{ "message_from_r": "your table has been written to %s" }\n', params$filename))
