
class NotImplementedMethodError(NotImplementedError):
    """Exception raised when a method has not been fully implemented yet.

    This exception is raised when a method has been already defined but its code was not fully
    implemented yet. Maybe the method was just included in a developing version to be coded in the
    future. Or maybe the method works already for certain values of the input arguments, but not
    for others yet.

    Note
    ----
    This exception does not require input arguments.

    Raises
    ------
    NotImplementedMethodError
        A message is printed out with the name of the method raising the exception, the link to
        the API documentation, and the link to the issues board of Sabueso's GitHub repository.

    Examples
    --------
    >>> from sabueso._private_tools.exceptions import NotImplementedMethodError
    >>> def method_name(a, b=True):
    ...    raise NotImplementedMethodError
    ...    pass

    .. admonition:: See Also
       :class: attention

        :doc:`Exceptions' section in the Developer Guide documentation </docs/contents/developer/exceptions.ipynb>`

    """

    def __init__(self):

        from sabueso import __github_issues_web__
        from inspect import stack

        all_stack_frames = stack()
        caller_stack_frame = all_stack_frames[1]
        caller_name = caller_stack_frame[3]

        method_name = caller_name
        api_doc = ''

        message = (
                f"The \"{method_name}\" method has not been implemented yet in the way you are using it. "
                f"Check {api_doc} for more information. "
                f"If you still want to suggest its implementation, open a new issue in {__github_issues_web__}"
                )

        super().__init__(message)


class NotImplementedClassError(NotImplementedError):
    """Exception raised when a class has not been fully implemented yet.

    This exception is raised when a class has being already defined but its code was not fully
    implemented yet. Maybe the class was just included in a developing version to be coded in the
    future. Or maybe the class can be instantated already for certain values of the input
    arguments, but not for others yet.

    Note
    ----
    This exception does not require input arguments.

    Raises
    ------
    NotImplementedClassError
        A message is printed out with the name of the class raising the exception, the link to
        the API documentation, and the link to the issues board of Sabueso's GitHub repository.

    Examples
    --------
    >>> from sabueso._private_tools.exceptions import NotImplementedClassError
    >>> class ClassName():
    ...    def __init__(self):
    ...       raise NotImplementedClassError
    ...       pass

    .. admonition:: See Also
       :class: attention

        :doc:`Exceptions' section in the Developer Guide documentation </docs/contents/developer/exceptions.ipynb>`

    """

    def __init__(self):

        from sabueso import __github_issues_web__
        from inspect import stack

        all_stack_frames = stack()
        caller_stack_frame = all_stack_frames[1]
        caller_name = caller_stack_frame[3]

        class_name = caller_name
        api_doc = ''

        message = (
                f"The \"{class_name}\" class has not been implemented yet in the way you are using it. "
                f"Check {api_doc} for more information. "
                f"If you still want to suggest its implementation, open a new issue in {__github_issues_web__}."
                )

        super().__init__(message)


class NotImplementedFormError(NotImplementedError):
    """Exception raised when a method or a class does not support a specific item's form yet.

    This exception is raised when a method or a class should be able to work with an item's form,
    but it has not been implemented yet. For instance, a method gets the number of atoms of a
    molecular system, but the current version works over a pdb file but not yet over a mol file. In
    this case this exception should be rised when the input argument is a mol file.

    Parameters
    ----------
    form : str
        The item's form not supported yet.

    Raises
    ------
    NotImplementedFormError
        A message is printed out with the name of the not supported form, the name of the class or
        the method raising the exception, the link to the API documentation, and the link to the
        issues board of Sabueso's GitHub repository.

    Examples
    --------
    >>> from sabueso._private_tools.exceptions import NotImplementedFormError
    >>> from sabueso import get_form
    >>> def method_name(item):
    ...    input_form = get_form(item)
    ...    if input_form not in ['file:pdb', 'string:pdb_id', 'string:pdb_text']:
    ...       raise NotImplementedFormError(input_form)
    ...    pass

    .. admonition:: See Also
       :class: attention

        :doc:`Exceptions' section in the Developer Guide documentation </docs/contents/developer/exceptions.ipynb>`

    """

    def __init__(self, form):

        from sabueso import __github_issues_web__

        message = (
                f"The \"{form}\" form has not been implemeted yet in the way you are using it. "
                f"Write a new issue in {__github_issues_web__} asking for its implementation."
                )

        super().__init__(message)


class WrongFormError(ValueError):

    def __init__(self, form):

        from sabueso import __github_issues_web__
        from inspect import stack

        all_stack_frames = stack()
        caller_stack_frame = all_stack_frames[1]
        caller_name = caller_stack_frame[3]

        method_name = caller_name
        api_doc = ''

        message = (
                f"The input item's form in the \"{method_name}\" method must be {form}. "
                f"Check {api_doc} for more information. "
                f"If you still need help, open a new issue in {__github_issues_web__}"
                )

        super().__init__(message)


class NotWithThisFormError(ValueError):

    def __init__(self, form):

        from sabueso import __github_issues_web__
        from inspect import stack

        all_stack_frames = stack()
        caller_stack_frame = all_stack_frames[1]
        caller_name = caller_stack_frame[3]

        method_name = caller_name
        api_doc = ''

        message = (
                f"The \"{method_name}\" method does not work with {form} items. "
                f"Check {api_doc} for more information. "
                f"If you still need help, open a new issue in {__github_issues_web__}"
                )

        super().__init__(message)


class UnknownFormError(ValueError):

    def __init__(self, form):

        from sabueso import __github_issues_web__
        from inspect import stack

        all_stack_frames = stack()
        caller_stack_frame = all_stack_frames[1]
        caller_name = caller_stack_frame[3]

        method_name = caller_name
        api_doc = ''

        message = (
                f"The input item's form in the \"{method_name}\" method must be {form}. "
                f"Check {api_doc} for more information. "
                f"If you still need help, open a new issue in {__github_issues_web__}"
                )

        super().__init__(message)


class BadCallError(ValueError):

    def __init__(self, argument=None):

        from sabueso import __github_issues_web__
        from inspect import stack

        all_stack_frames = stack()
        caller_stack_frame = all_stack_frames[1]
        caller_name = caller_stack_frame[3]

        method_name = caller_name
        api_doc = ''

        message = f"The \"{method_name}\" method was not properly invoked"
        if argument is not None:
            message += f", probably due to the \"{argument}\" input argument"
        message += (
                f". Check {api_doc} for more information. "
                f"If you still need help, open a new issue in {__github_issues_web__}"
                )

        super().__init__(message)

class LibraryNotFoundError(NotImplementedError):

    def __init__(self, library):

        from sabueso import __github_issues_web__
        from inspect import stack

        all_stack_frames = stack()
        caller_stack_frame = all_stack_frames[1]
        caller_name = caller_stack_frame[3]

        method_name = caller_name
        api_doc = ''

        message = (
                f"The python library {library} was not found. "
                f"Although {library} is not considered a dependency, it needs "
                f"to be installed to execute the {method_name} method the way you require. "
                f"If you still need help, open a new issue in {__github_issues_web__}."
                )

        super().__init__(message)

class DatabaseNotAccessibleError(NotImplementedError):

    def __init__(self, database):

        from sabueso import __github_issues_web__

        message = (
                f"The online database {database} cannot be reached. "
                f"Check your internet connection and the availability of {database}"
                f"If you still need help, open a new issue in {__github_issues_web__}."
                )

        super().__init__(message)

