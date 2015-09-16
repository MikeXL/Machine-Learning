require(httr)
require(jsonlite)

# account key here
# account key shown on the http://datamarket.azure.com my account page
account_key <- "AccountKey:<your account key here>"
secret <- RCurl::base64(account_key)

# the sentiment batch URL
sentiment_url <- 'https://api.datamarket.azure.com/data.ashx/amla/text-analytics/v1/GetSentimentBatch'

# assuming the text in the data frame named sentiment.text
# column names: Id, Text
# as of September, 2015 the API supports up to 1000 texts in one batch call
params <- paste("{Inputs:", toJSON(sentiment.text), "}")

req <- POST(sentiment_url,
            add_headers(
                        "Content-Type"  = paste("application/json"),
                        "Authorization" = paste("Basic", secret)
                        ),
            body = paste(params)
            )

#token <- paste("Bearer", content(req)$access_token)

# parse the result into data frame
json <- content(req, as="text")
sentiments <- fromJSON(json)
