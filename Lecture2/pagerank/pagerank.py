import os
import random
import re
import sys
import math

DAMPING = 0.85
SAMPLES = 10000


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}
    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )

    return pages


def transition_model(corpus, page, damping_factor):
    """
    Return a probability distribution over which page to visit next,
    given a current page.

    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.
    """
    returnVal = {}
    pagesLen = corpus[page]
    dictLen = corpus.keys()
    #Use page rank formula PR = (1-d)/p + sum(d/p) 
    if len(pagesLen) != 0:    
        for p in (dictLen):   
            if p in pagesLen: 
                returnVal[p] = (1 - damping_factor)/len(dictLen) + damping_factor / len(pagesLen)
            else:
                returnVal[p] = (1 - damping_factor)/len(dictLen)
    #If no referneces are made, all pages have equal probability
    else: 
        for p in dictLen:
            returnVal[p] = 1/len(dictLen)
    return returnVal
    raise NotImplementedError


def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    returnVal = corpus.copy() 
    for p in ((corpus)):
        returnVal[p] = 0
    page = None
    for num in range(n):
        #treat each probability as a range (ie 1.html=[0, 0.2] (20%), 2.html=[0.2, 0.81] (61%))
        #Generate a random number, the range of this number is its page
        if page:  
            probVal = transition_model(corpus, page, damping_factor)
            totSum = 0
            temp = random.random()
            for p in probVal: 
                if temp <= totSum + probVal[p]:
                    page = p
                    break
                else: 
                    totSum += probVal[p]
        #If no page is referenced, randomly select
        #Increment the page count after every interation
        else: 
            page = random.choice(list(corpus.keys()))
        returnVal[str(page)] += 1   
    #Divide by to compute page rank
    for pages in returnVal: 
        returnVal[pages] /= n 
    return returnVal
    raise NotImplementedError


def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    copyCorp = corpus.copy() 
    new = {}
    for n in ((corpus)):
        copyCorp[n] = 1/len(corpus) 
    #Iteratively sum for page rank (PR = (1-d)/p + sum(d/p) )
    while True:
        for p in copyCorp:
            temp = 0
            #Increment each time page is refernced
            #Implement formula and update 'new' dictionary
            for page in copyCorp: 
                if p in corpus[page]: temp += copyCorp[page]/len(corpus[page]) 
                if len(corpus[page]) == 0: temp += copyCorp[page]/len(copyCorp) 
            temp = (1-damping_factor)/len(copyCorp) + temp*damping_factor 
            new[p] = temp
        #Check if page rank has changed by less than 0.001
        maxTemp = 0
        for x in copyCorp: 
            maxNow = abs(new[x] - copyCorp[x])
            if maxNow > maxTemp: maxTemp = maxNow
        if maxTemp < 0.001: break
        copyCorp = new.copy()
    return copyCorp
    raise NotImplementedError

if __name__ == "__main__":
    main()
