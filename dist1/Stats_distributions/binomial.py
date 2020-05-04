import math
import matplotlib.pyplot as plt
from .general_distribution import Distribution

class Binomial(Distribution):
    """ Binomial distribution class for calculating and 
    visualizing a Binomial distribution.
    
    Attributes:
        mean (float) representing the mean value of the distribution
        stdev (float) representing the standard deviation of the distribution
        data_list (list of floats) a list of floats to be extracted from the data file
        p (float) representing the probability of an event occurring
        n (int) the total number of trials
    
    
    """
    
    
    def __init__(self, prob=.5, size=20):
        self.p = prob
        self.n = size
        self.mean = self.calculate_mean()
        self.stdev = self.calculate_stdev()
        Distribution.__init__(self, self.mean, self.stdev)
    
        
        
    
    def calculate_mean(self):
    
        """Function to calculate the mean from p and n
        
        Args: 
            None
        
        Returns: 
            float: mean of the data set
    
        """
        return self.n*self.p                
        



    def calculate_stdev(self):

        """Function to calculate the standard deviation from p and n.
        
        Args: 
            None
        
        Returns: 
            float: standard deviation of the data set
    
        """
        return math.sqrt(self.n*self.p*(1-self.p))
     
        
        
        
    def replace_stats_with_data(self):
    
        """Function to calculate p and n from the data set
        
        Args: 
            None
        
        Returns: 
            float: the p value
            float: the n value
    
        """        
        
        self.n = len(self.data)
        self.p = sum(self.data)/self.n
        self.mean = self.calculate_mean()
        self.stdev = self.calculate_stdev()
        
        return self.p, self.n
        


    def plot_bar(self):
        """Function to output a histogram of the instance variable data using 
        matplotlib pyplot library.
        
        Args:
            None
            
        Returns:
            None
        """
            
        plt.bar(x=['0', '1'], y = [self.n*(1-self.p), self.n*(self.p)])
        plt.title('Bar Chart of Data')
        plt.xlabel('outcome')
        plt.ylabel('count')



    def pdf(self, k):
        """Probability density function calculator for the gaussian distribution.
        
        Args:
            k (float): point for calculating the probability density function
            
        
        Returns:
            float: probability density function output
        """
        
        
        a = math.factorial(self.n) / (math.factorial(k) * (math.factorial(self.n - k)))
        b = (self.p ** k) * (1 - self.p) ** (self.n - k)
        
        return a * b 

    def plot_bar_pdf(self):

        """Function to plot the pdf of the binomial distribution
        
        Args:
            None
        
        Returns:
            list: x values for the pdf plot
            list: y values for the pdf plot
            
        """
    
        # TODO: Use a bar chart to plot the probability density function from
        # k = 0 to k = n
        
        #   Hint: You'll need to use the pdf() method defined above to calculate the
        #   density function for every value of k.
        
        #   Be sure to label the bar chart with a title, x label and y label

        #   This method should also return the x and y values used to make the chart
        #   The x and y values should be stored in separate lists
        xs = range(0, self.n+1)
        ys = [self.pdf(x) for x in xs]
        plt.figure(figsize=(16,7))
        plt.bar(xs, ys)
        plt.title('Bar Chart of PDF')
        plt.xlabel('k')
        plt.ylabel('Probability')
                
    def __add__(self, other):
        
        """Function to add together two Binomial distributions with equal p
        
        Args:
            other (Binomial): Binomial instance
            
        Returns:
            Binomial: Binomial distribution
            
        """
        
        try:
            assert self.p == other.p, 'p values are not equal'
        except AssertionError as error:
            raise error
        
        # TODO: Define addition for two binomial distributions. Assume that the
        # p values of the two distributions are the same. The formula for 
        # summing two binomial distributions with different p values is more complicated,
        # so you are only expected to implement the case for two distributions with equal p.
        
        # the try, except statement above will raise an exception if the p values are not equal
        
        # Hint: You need to instantiate a new binomial object with the correct n, p, 
        #   mean and standard deviation values. The __add__ method should return this
        #   new binomial object.
        
        #   When adding two binomial distributions, the p value remains the same
        #   The new n value is the sum of the n values of the two distributions.
        new_p = self.p
        new_n = self.n+other.n
        binomial = Binomial(new_p, new_n)
        return binomial
                
        
    def __repr__(self):
    
        """Function to output the characteristics of the Binomial instance
        
        Args:
            None
        
        Returns:
            string: characteristics of the Gaussian
        
        """
        
        # TODO: Define the representation method so that the output looks like
        #       mean 5, standard deviation 4.5, p .8, n 20
        #
        #       with the values replaced by whatever the actual distributions values are
        #       The method should return a string in the expected format
    
        return f"mean {self.mean}, standard deviation {self.stdev}, p {self.p}, n {self.n}"
