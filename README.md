# Value investing powered by modern machine learning
Working on developing a simple custom loss function for basic value investing application.
Investing like Warren Buffet using Neural Networks 

Warren Buffet’s legendary investment process sounds extraordinarily simple. He understands the fundamental financial data of a company to determine whether it is undervalued, fairly priced or overpriced. Doing this individually for hundreds of companies is inherently challenging.  

This fundamental financial data includes the company’s P/E ratio, liquidity, solvency and the amount of cash it currently has. All this data provides a proxy for assessing a stock’s value. In this repository I built a neural network to perform the same type of analysis in an automated manner.  

I wanted to automate the complex process by creating a neural network built on stock data which takes the pure financial data of a company, and outputs it’s price. If this could be done amongst several stocks, we could then find an effective encoding of valuation based purely on fundamental financial analysis. The neural network I used in this project was implemented with a custom quartic loss function. The reasoning behind this is that I wanted to penalize large differences in prediction far more than small losses and a quartic loss function would be better at doing this than a regular quadratic loss function. 

We then might be able to apply the same model to new stocks to see their predicted price relative to their actual price. If the predicted price is lower than the actual price, it might be worth analyzing this company individually and attempting to determine whether the equity stock is an attractive stock to purchase.  
