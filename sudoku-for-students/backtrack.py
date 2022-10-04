We the undersigned promise that we have in good faith attempted to follow the 
principles of pair programming. Although we were free to discuss ideas with 
others, the implementation is our own. We have shared a common workspace 
(possibly virtually) and taken turns at the keyboard for the majority of the 
work that we are submitting. Furthermore, any non programming portions of the 
assignment were done independently. We recognize that should this not be the 
case, we will be subject to penalties as outlined in the course syllabus. 
[Phillip Cuesta and Kaitlyn Nguyen]



from csp_lib.backtrack_util import (first_unassigned_variable, 
                                    unordered_domain_values,
                                    no_inference)

def backtracking_search(csp,
                        select_unassigned_variable=first_unassigned_variable,
                        order_domain_values=unordered_domain_values,
                        inference=no_inference,
                        verbose=False):
    """backtracking_search
    Given a constraint satisfaction problem (CSP),
    a function handle for selecting variables, 
    a function handle for selecting elements of a domain,
    and a function handle for making inferences after assignment,
    solve the CSP using backtrack search

    If verbose is True, prints number of assignments and inferences

    Returns two outputs:
       dictionary of assignments or None if there is no solution
       Number of variable assignments made in backtrack search (not counting
       assignments made by inference)
    """
    
    # See Figure 6.5 of your book for details

    raise notImplemented
