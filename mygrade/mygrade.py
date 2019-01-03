"""TO-DO: Write a description of what this XBlock is."""

import pkg_resources
from xblock.core import XBlock
from xblock.fields import Integer, Scope
# from xblock.fragment import Fragment

from web_fragments.fragment import Fragment
# from xmodule.x_module import XModule, module_attr, STUDENT_VIEW


class MygradeXBlock(XBlock):
    """
    TO-DO: document what your XBlock does.
    """

    # Fields are defined on the class.  You can access them in your code as
    # self.<fieldname>.

    # TO-DO: delete count, and define your own fields.
    count = Integer(
        default=0, scope=Scope.user_state,
        help="A simple counter, to show something happening",
    )

    def resource_string(self, path):
        """Handy helper for getting resources from our kit."""
        data = pkg_resources.resource_string(__name__, path)
        return data.decode("utf8")

    # TO-DO: change this view to display your data your own way.
    # def student_view(self, context=None):
    #     """
    #     The primary view of the MygradeXBlock, shown to students
    #     when viewing courses.
    #     """
    #     html = self.resource_string("static/html/mygrade.html")
    #     frag = Fragment(html.format(self=self))
    #     frag.add_css(self.resource_string("static/css/mygrade.css"))
    #     frag.add_javascript(self.resource_string("static/js/src/mygrade.js"))
    #     frag.initialize_js('MygradeXBlock')
    #     return frag

    def student_view(self, context):
        """
        Renders the contents of the chosen condition for students, and all the
        conditions for staff.
        """
        # if self.child is None:
        #     # raise error instead?  In fact, could complain on descriptor load...
        #     return Fragment(content=u"<div>Nothing here.  Move along.</div>")
        #
        # if self.system.user_is_staff:
        #     return self._staff_view(context)
        # else:

        # child_fragment = self.render(Fragment(self.get_html()), context)
        context = {"count": self.count}
        fragment = Fragment(self.system.render_template('static/html/mygrade.html', context))
        # fragment.add_fragment_resources(child_fragment)
        fragment.add_css(self.resource_string("static/css/mygrade.css"))
        fragment.add_javascript_url(self.runtime.local_resource_url(self, 'static/js/src/mygrade.js'))
        fragment.initialize_js('MygradeXBlock')
        return fragment

    # TO-DO: change this handler to perform your own actions.  You may need more
    # than one handler, or you may not need any handlers at all.
    @XBlock.json_handler
    def increment_count(self, data, suffix=''):
        """
        An example handler, which increments the data.
        """
        # Just to show data coming in...
        assert data['hello'] == 'world'

        self.count += 1
        return {"count": self.count}

    # TO-DO: change this to create the scenarios you'd like to see in the
    # workbench while developing your XBlock.
    @staticmethod
    def workbench_scenarios():
        """A canned scenario for display in the workbench."""
        return [
            ("MygradeXBlock",
             """<mygrade/>
             """),
            ("Multiple MygradeXBlock",
             """<vertical_demo>
                <mygrade/>
                <mygrade/>
                <mygrade/>
                </vertical_demo>
             """),
        ]
