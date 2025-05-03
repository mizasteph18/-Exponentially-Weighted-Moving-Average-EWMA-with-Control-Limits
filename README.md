# -Exponentially-Weighted-Moving-Average-EWMA-with-Control-Limits

Recommended Approach
Given the need to emphasize recent data and the potential for portfolio changes, the Exponentially Weighted Moving Average (EWMA) with Control Limits is a strong candidate. It is relatively simple to implement and interpret, and the weighting scheme directly addresses the recency bias requirement.
Steps to implement this approach:
 * Calculate EWMA: Choose a decay factor (\alpha) between 0 and 1. A smaller \alpha gives more weight to recent data. Calculate the EWMA of your stress test figures over time using the formula:
   EWMA_t = \alpha \cdot Value_t + (1 - \alpha) \cdot EWMA_{t-1}
   where EWMA_0 can be initialized with the first data point.
 * Establish Control Limits: Calculate the standard deviation of the EWMA or, more commonly, the standard deviation of the original data within a recent window or using an exponentially weighted approach as well. Then, set upper and lower control limits, typically at \pm 2 or \pm 3 standard deviations from the EWMA. The choice of the number of standard deviations depends on the desired sensitivity to outliers.
 * Assess the Latest Figure: Compare the latest stress test figure to these control limits. If it falls outside the limits, it can be flagged as a potential outlier.

This approach provides a dynamic way to assess outliers in your time series data, giving more weight to recent observations, which aligns with your requirement. Remember to fine-tune the decay factor (\alpha) and the number of standard deviations for the control limits based on your specific data and the level of sensitivity you need for outlier detection. You might also want to visualize the stress test figures along with the EWMA and control limits to better understand the identified outliers.
