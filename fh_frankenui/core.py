"""The building blocks to the UI"""

# AUTOGENERATED! DO NOT EDIT! File to edit: ../lib_nbs/00_core.ipynb.

# %% auto 0
__all__ = ['stringify', 'VEnum', 'Theme', 'TextB', 'TextT', 'UkIcon', 'DiceBearAvatar', 'FlexT', 'GridT', 'Grid',
           'ResponsiveGrid', 'FullySpacedDiv', 'CenteredDiv', 'LAlignedDiv', 'RAlignedDiv', 'VStackedDiv',
           'HStackedDiv', 'SpaceBetweenDiv', 'UkGenericInput', 'UkInput', 'UkSwitch', 'UkCheckbox', 'UkTextArea',
           'UkFormLabel', 'UkButtonT', 'UkButton', 'UkIconButton', 'Options', 'UkSelect', 'UkDropdownButton',
           'UkGenericComponent', 'UkH1', 'UkH2', 'UkH3', 'UkH4', 'UkH5', 'UkH6', 'UkHSplit', 'UkHLine', 'UkNavDivider',
           'UkNavbarDropdown', 'UkNavbar', 'NavTab', 'UkTab', 'UkSidebarItem', 'UkSidebarUl', 'UkSidebarSection',
           'UkSidebar', 'Card', 'UkModalTitle', 'Modal', 'TableHeader', 'TableRow', 'UkTable', 'UkFormSection']

# %% ../lib_nbs/00_core.ipynb
from fasthtml.common import *
from fasthtml.svg import Svg
from enum import Enum
from fasthtml.components import Uk_select,Uk_input_tag
from functools import partial
from itertools import zip_longest
from typing import Union, Tuple, Optional
from fastcore.all import L, delegates

# %% ../lib_nbs/00_core.ipynb
# need a better name, stringify might be too general for what it does 
def stringify(o # String, Tuple, or Enum options we want stringified
             ): # String that can be passed FT comp args (such as `cls=`)
    "Converts input types into strings that can be passed to FT components"  
    if is_listy(o): return ' '.join(map(str,o)) if o else ""
    return o.__str__()

# %% ../lib_nbs/00_core.ipynb
class VEnum(Enum):
    def __add__(self, other):
        "Add other enums, listy, or strings"
        return stringify((self, other))

    def __radd__(self, other):
        "Add other enums, listy, or strings"
        return stringify((other, self))    
    
    def __str__(self):
        base = self.__class__.__name__.lstrip('Uk').rstrip('T')
        return f"uk-{base.lower()}-{self.value}".strip('-')

# %% ../lib_nbs/00_core.ipynb
class Theme(Enum):
    slate = "slate"
    stone = "stone"
    gray = "gray"
    neutral = "neutral"
    red = "red"
    rose = "rose"
    orange = "orange"
    green = "green"
    blue = "blue"
    yellow = "yellow"
    violet = "violet"
    zinc = "zinc"

    def headers(self):
        js = (Script(src="https://cdn.tailwindcss.com"),
              Script(src="https://cdn.jsdelivr.net/npm/uikit@3.21.6/dist/js/uikit.min.js"),
              Script(src="https://cdn.jsdelivr.net/npm/uikit@3.21.6/dist/js/uikit-icons.min.js"),
              Script(type="module", src="https://unpkg.com/franken-wc@0.0.6/dist/js/wc.iife.js")
              )
        _url = f"https://unpkg.com/franken-wc@0.0.6/dist/css/{self.value}.min.css"
        return (*js, Link(rel="stylesheet", href=_url))

# %% ../lib_nbs/00_core.ipynb
class TextB(Enum):
    sz_xsmall = 'text-xs'
    sz_small = 'text-sm'
    sz_medium = 'text-base'
    sz_large = 'text-lg'
    cl_muted = 'uk-text-muted'
    
    wt_light = 'font-light'
    wt_normal = 'font-normal'
    wt_medium = 'font-medium'
    wt_bold = 'font-bold'
    
    def __str__(self): return stringify(self.value)

# %% ../lib_nbs/00_core.ipynb
class TextT(Enum):
    muted_xs =  TextB.sz_xsmall, TextB.cl_muted 
    muted_sm =  TextB.sz_small,  TextB.cl_muted # Text below card headings
    muted_med = TextB.sz_medium, TextB.cl_muted 
    muted_lg =  TextB.sz_large,  TextB.cl_muted 
    medium_sm = TextB.sz_small,  TextB.wt_medium
    medium_xs = TextB.sz_xsmall, TextB.wt_medium

    def __str__(self): return stringify(self.value)

# %% ../lib_nbs/00_core.ipynb
def UkIcon(icon,    # Icon name from https://getuikit.com/docs/icon
           ratio=1, # Icon ratio/size 
           cls=()   # Span classes
          ):        # Span with Icon
    "Creates a Span with the given icon"
    return Span(uk_icon=f"icon: {icon}; ratio: {ratio}",cls=stringify(cls))

# %% ../lib_nbs/00_core.ipynb
def DiceBearAvatar(seed_name, # Seed name (ie 'Isaac Flath')
                   h,         # Height 
                   w          # Width
                  ):          # Span with Avatar
    url = 'https://api.dicebear.com/8.x/lorelei/svg?seed='
    return Span(cls=f"relative flex h-{h} w-{w} shrink-0 overflow-hidden rounded-full bg-accent")(
            Img(cls="aspect-square h-full w-full", alt="Avatar", src=f"{url}{seed_name}"))

# %% ../lib_nbs/00_core.ipynb
class FlexT(VEnum):
    block       = ''
    inline      = 'inline'
    #horizontal
    left        = 'left'
    center      = 'center'
    right       = 'right'
    between     = 'between'
    around      = 'around'
    #vertical
    stretch     = 'stretch'
    top         = 'top'
    middle      = 'middle'
    botton      = 'bottom'
    #direction
    row         = 'row'
    row_reverse = 'row-reverse'
    col         = 'col'
    col_reverse = 'col-reverse'
    #wrap
    nowrap      = 'nowrap'
    wrap        = 'wrap'
    wrap_reverse= 'wrap-reverse'

# %% ../lib_nbs/00_core.ipynb
class GridT(VEnum):
    # gap
    small  = 'small'
    medium = 'medium'
    large  = 'large'
    none   = 'collapse'

# %% ../lib_nbs/00_core.ipynb
def Grid(*c,      # Divs/Containers that should be divided into a grid
         cols=3,  # Number of columns
         cls=(),  # Additional classes for Grid Div
         **kwargs # Additional args for Grid Div
        ):
    """Creates a grid with the given number of columns, often used for a grid of cards"""
    cls = stringify(cls)
    return Div(cls=(f'grid grid-cols-{cols}',cls), **kwargs)(*c)

# %% ../lib_nbs/00_core.ipynb
def ResponsiveGrid(*c, sm=1, md=2, lg=3, xl=4, gap=2, cls='', **kwargs):
    "Creates a responsive grid with the given number of columns for different screen sizes"
    return Div(cls=f'grid grid-cols-{sm} md:grid-cols-{md} lg:grid-cols-{lg} xl:grid-cols-{xl} gap-{gap} ' + stringify(cls), **kwargs)(*c)

# %% ../lib_nbs/00_core.ipynb
def FullySpacedDiv(*c,                # Components
                   cls='uk-width-1-1',# Classes for outer div
                   **kwargs           # Additional args for outer div
                  ):                  # Div with spaced components via flex classes
    "Creates a flex div with it's components having as much space between them as possible"
    cls = stringify(cls)
    return Div(cls=(FlexT.block,FlexT.between,FlexT.middle,cls), **kwargs)(*c)

# %% ../lib_nbs/00_core.ipynb
def CenteredDiv(*c,      # Components
                cls=(),  # Classes for outer div
                **kwargs # Additional args for outer div
               ): # Div with components centered in it
    "Creates a flex div with it's components centered in it"
    cls=stringify(cls)
    return Div(cls=(FlexT.block,FlexT.col,FlexT.middle,FlexT.center,cls),**kwargs)(*c)

# %% ../lib_nbs/00_core.ipynb
def LAlignedDiv(*c,      # Components
                cls=(),  # Classes for outer div
                **kwargs # Additional args for outer div
               ): # Div with components aligned to the left
    "Creates a flex div with it's components aligned to the left"
    cls=stringify(cls)
    return Div(cls=(FlexT.block,FlexT.left,FlexT.middle,cls), **kwargs)(*c)

# %% ../lib_nbs/00_core.ipynb
def RAlignedDiv(*c,      # Components
                cls=(),  # Classes for outer div
                **kwargs # Additional args for outer div
               ): # Div with components aligned to the right
    "Creates a flex div with it's components aligned to the right"
    cls=stringify(cls)
    return Div(cls=(FlexT.block,FlexT.right,FlexT.middle,cls), **kwargs)(*c)

# %% ../lib_nbs/00_core.ipynb
def VStackedDiv(*c, cls='', **kwargs):
    cls=stringify(cls)
    return Div(cls=(FlexT.block,FlexT.col,FlexT.middle,cls), **kwargs)(*c)

# %% ../lib_nbs/00_core.ipynb
def HStackedDiv(*c, cls='', **kwargs):
    cls=stringify(cls)
    return Div(cls=(FlexT.block,FlexT.row,FlexT.middle,cls), **kwargs)(*c)

# %% ../lib_nbs/00_core.ipynb
def SpaceBetweenDiv(*c, cls='', **kwargs):
    cls = stringify(cls)
    return Div(cls=(FlexT.block,FlexT.between,FlexT.middle,cls), **kwargs)(*c)

# %% ../lib_nbs/00_core.ipynb
def UkGenericInput(input_fn: FT, # FT Components that generates a user input (e.g. `TextArea`)
                    label:str|FT=(), # String or FT component that goes in `Label`
                    lbl_cls:str|Enum=(), # Additional classes that goes in `Label`
                    inp_cls:str|Enum='', # Additional classes that go in user input (e.g. `TextArea`)
                    cls:str|Enum=('space-y-2',), # Div cls
                    id: str="", # ID of the user input (e.g. `TextArea`)
                   **kwargs # Passed to `input_fn` (e.g. ` TextArea`)
                  ) -> FT: # FT component in structure `(Div(label,input))`
    "`Div(Label,Input)` component with Uk styling injected appropriately. Generally you should higher level API, such as `UKTextArea` which is created for you in this library"
    lbl_cls, inp_cls, cls = map(stringify,(lbl_cls, inp_cls, cls))
    if label:  label = Label(cls='uk-form-label '+lbl_cls, fr=id)(label)
    res = input_fn(cls=inp_cls, **kwargs)
    return Div(cls=cls)(label, res)

# %% ../lib_nbs/00_core.ipynb
@delegates(UkGenericInput,but=['input_fn','inp_cls'])
def UkInput(*args, inp_cls='', **kwargs): 
    "Creates a text input with uk styling"
    inp_cls = ('uk-input',stringify(inp_cls))
    return UkGenericInput(Input, *args, inp_cls=inp_cls, **kwargs)

# %% ../lib_nbs/00_core.ipynb
@delegates(UkGenericInput,but=['input_fn','inp_cls'])
def UkSwitch(*args, inp_cls='', **kwargs): 
    "Creates a switch input with uk styling"
    inp_cls = ('uk-toggle-switch uk-form-switch',stringify(inp_cls))
    return UkGenericInput(CheckboxX, *args, inp_cls=inp_cls, **kwargs)

# %% ../lib_nbs/00_core.ipynb
@delegates(UkGenericInput,but=['input_fn','inp_cls'])
def UkCheckbox(*args, inp_cls='', **kwargs): 
    "Creates a checkbox input with uk styling"
    inp_cls = ('uk-checkbox',stringify(inp_cls))
    return UkGenericInput(CheckboxX, *args, inp_cls=inp_cls, **kwargs)

# %% ../lib_nbs/00_core.ipynb
@delegates(UkGenericInput,but=['input_fn','inp_cls'])
def UkTextArea(*args, inp_cls='', **kwargs): 
    "Creates a textarea with uk styling"
    inp_cls = ('uk-textarea',stringify(inp_cls))
    return UkGenericInput(Textarea, *args, inp_cls=inp_cls,  **kwargs)

# %% ../lib_nbs/00_core.ipynb
@delegates(UkGenericInput,but=['input_fn','inp_cls'])
def UkFormLabel(*args, inp_cls='', **kwargs): 
    "Creates a form label with uk styling"
    inp_cls = ('uk-form-label',stringify(inp_cls))
    return UkGenericInput(Uk_input_tag ,*args, inp_cls=inp_cls, **kwargs)

# %% ../lib_nbs/00_core.ipynb
class UkButtonT(VEnum):
    default   = 'default'
    primary   = 'primary'
    secondary = 'secondary'
    danger    = 'danger'
    ghost     = 'ghost'
    text      = 'text'
    link      = 'link'

# %% ../lib_nbs/00_core.ipynb
def UkButton(*c, 
            cls=UkButtonT.default, # Use UkButtonT or styles 
            **kwargs):    
    return Button(type='button', cls='uk-button ' + stringify(cls), **kwargs)(*c)

# %% ../lib_nbs/00_core.ipynb
def UkIconButton(*c, sz='small', cls=(), **kwargs):
    if sz not in ('small','medium','large'): raise ValueError(f"Invalid size '{sz}'. Must be 'small', 'medium', or 'large'.")
    return Button(cls=f'uk-icon-button uk-icon-button-{sz} ' + stringify(cls), **kwargs)(*c)

# %% ../lib_nbs/00_core.ipynb
def Options(*c,                    # Content for an `Option`
            selected_idx:int=None, # Index location of selected `Option`
            disabled_idxs:set=None # Idex locations of disabled `Options`
           ):
    "Helper function to wrap things into `Option`s for use in `UKSelect`"
    return [Option(o,selected=i==selected_idx, disabled=disabled_idxs and i in disabled_idxs) for i,o in enumerate(c)]

# %% ../lib_nbs/00_core.ipynb
def UkSelect(*option,            # Options for the select dropdown (can use `Options` helper function to create)
             label=(),           # String or FT component for the label
             lbl_cls=(),         # Additional classes for the label
             inp_cls=(),         # Additional classes for the select input
             cls=('space-y-2',), # Classes for the outer div
             id="",              # ID for the select input
             name="",            # Name attribute for the select input
             placeholder="",     # Placeholder text for the select input
             searchable=False,   # Whether the select should be searchable
             **kwargs):          # Additional arguments passed to Uk_select
    "Creates a select dropdown with uk styling"
    lbl_cls, inp_cls, cls = map(stringify, (lbl_cls, inp_cls, cls))
    if label:
        lbl = Label(cls=f'uk-form-label {lbl_cls}', fr=id)(label) if id else Label(cls=f'uk-form-label {lbl_cls}')(label)
    select = Uk_select(cls=inp_cls, uk_cloak=True, id=id, name=name, placeholder=placeholder, searchable=searchable, **kwargs)
    select = select(*option)
    return Div(cls=cls)(lbl, select) if label else Div(cls=cls)(select)

# %% ../lib_nbs/00_core.ipynb
def _UkDropdownButtonOptions(opt_grps, opt_hdrs=None):
    res = []
    for g,h in zip_longest(opt_grps, tuplify(opt_hdrs)):
        if h: res.append(Li(cls="uk-nav-header")(h if isinstance(h,FT) else Div(h)))
        if isinstance(g,(list,tuple)): res += list(map(Li, g))
        else: res.append(Li(g))
    return res

# %% ../lib_nbs/00_core.ipynb
def UkDropdownButton(
    *opt_grp,        # List of options to be displayed in the dropdown
    opt_hdrs=None,  # List of headers for each option group, or None
    label=None,     # String, FT component, or None for the `Button`
    btn_cls=UkButtonT.default,  # Button class(es)
    cls=(),         # Parent div class
    dd_cls=(),      # Class that goes on the dropdown container
    icon='triangle-down',  # Icon to use for the dropdown
    icon_cls='',    # Additional classes for the icon
    icon_position='right'  # Position of the icon: 'left' or 'right'
    ):
    dd_cls, btn_cls, cls, icon_cls = map(stringify, (dd_cls, btn_cls, cls, icon_cls))
    icon_component = UkIcon(icon, cls=icon_cls) if icon else None
    btn_content = [] if label is None else [label]
    if icon_component: btn_content.insert(0 if icon_position == 'left' else len(btn_content), icon_component)
    btn = Button(type='button', cls='uk-button ' + btn_cls)(*btn_content)
    dd = Div(uk_dropdown='mode: click; pos: bottom-right', cls='uk-dropdown uk-drop ' + dd_cls)(
        Ul(cls='uk-dropdown-nav')(*_UkDropdownButtonOptions(opt_grp, opt_hdrs)))
    return Div(cls=cls)(Div(cls='flex items-center space-x-4')(btn, dd))

# %% ../lib_nbs/00_core.ipynb
def UkGenericComponent(component_fn, *c, cls=(), **kwargs):
    res = component_fn(cls=cls, **kwargs)(*c)
    return res

# %% ../lib_nbs/00_core.ipynb
def UkH1(*c, cls=(), **kwargs): return UkGenericComponent(H1, *c, cls='uk-h1 '+stringify(cls), **kwargs)
def UkH2(*c, cls=(), **kwargs): return UkGenericComponent(H2, *c, cls='uk-h2 '+stringify(cls), **kwargs)
def UkH3(*c, cls=(), **kwargs): return UkGenericComponent(H3, *c, cls='uk-h3 '+stringify(cls), **kwargs)
def UkH4(*c, cls=(), **kwargs): return UkGenericComponent(H4, *c, cls='uk-h4 '+stringify(cls), **kwargs)
def UkH5(*c, cls=(), **kwargs): return UkGenericComponent(H5, *c, cls='uk-h5 '+stringify(cls), **kwargs)
def UkH6(*c, cls=(), **kwargs): return UkGenericComponent(H6, *c, cls='uk-h6 '+stringify(cls), **kwargs)

# %% ../lib_nbs/00_core.ipynb
def UkHSplit(*c, cls=(), line_cls=(), text_cls=()):
    cls, line_cls, text_cls = map(stringify,(cls, line_cls, text_cls))
    return Div(cls='relative ' + cls)(
        Div(cls="absolute inset-0 flex items-center " + line_cls)(Span(cls="w-full border-t border-border")),
        Div(cls="relative flex justify-center " + text_cls)(Span(cls="bg-background px-2 ")(*c)))

# %% ../lib_nbs/00_core.ipynb
def UkHLine(lwidth=2, y_space=4): return Div(cls=f"my-{y_space} h-[{lwidth}px] w-full bg-secondary")

# %% ../lib_nbs/00_core.ipynb
def UkNavDivider(): return Li(cls="uk-nav-divider")

# %% ../lib_nbs/00_core.ipynb
def UkNavbarDropdown(*c, label, href='#', cls='', has_header=False, **kwargs):
    fn = lambda x: Li(item, cls='uk-drop-close', href='#demo', uk_toggle=True)
    flattened = []
    for i, item in enumerate(c):
        if i > 0: flattened.append(Li(cls="uk-nav-divider"))
        if isinstance(item, (list,tuple)): flattened.extend(map(Li, item))
        else: flattened.append(Li(item, cls="uk-nav-header" if i == 0 and has_header else None, uk_toggle=True))
    return (Li(cls=cls, **kwargs)(
                A(label, cls='uk-drop-close', href='#', uk_toggle=True), 
                Div(cls='uk-navbar-dropdown', uk_dropdown="mode: click; pos: bottom-left")(Ul(cls='uk-nav uk-dropdown-nav')(*flattened))))

# %% ../lib_nbs/00_core.ipynb
def _NavBarSide(n, s):
    def add_class(item):
        if isinstance(item, str): return Li(cls='uk-navbar-item')(item)
        else: item.attrs['class'] = f"{item.attrs.get('class', '')} uk-navbar-item".strip()
        return item
    return Div(cls=f'uk-navbar-{s}')(Ul(cls='uk-navbar-nav')(*map(add_class, tuplify(n))))

# %% ../lib_nbs/00_core.ipynb
def UkNavbar(lnav: Sequence[Union[str, FT]]=None, 
             rnav: Sequence[Union[str, FT]]=None, 
             cls='',
             **kwargs
            ) -> FT:
    return Div(cls='uk-navbar-container uk-width-1-1 relative z-10 '+ stringify(cls), uk_navbar=True, **kwargs)(
             _NavBarSide(lnav,'left') if lnav else '',
             _NavBarSide(rnav,'right') if rnav else '')

# %% ../lib_nbs/00_core.ipynb
def NavTab(text, active=False):
    return Li(cls="uk-active" if active else " ")(A(text, href="#demo", uk_toggle=True))

def UkTab(*items, maxw=96, cls='', **kwargs):
    cls = stringify(cls)
    return Ul(cls=f"uk-tab-alt max-w-{maxw} "+cls,**kwargs)(*[NavTab(item, active=i==0) for i, item in enumerate(items)])

# %% ../lib_nbs/00_core.ipynb
def UkSidebarItem(item, is_header=False): 
    return item if is_header else A(role='button')(item)

def UkSidebarUl(*lis, cls='space-y-2', **kwargs): 
    return Ul(cls=f"uk-nav uk-nav-secondary " + stringify(cls), **kwargs)(*map(Li,lis))

def UkSidebarSection(items, header=None, cls='', **kwargs):
    section = []
    if header: section.append(header)
    section += [UkSidebarItem(item) for item in items]
    return UkSidebarUl(*section, cls=stringify(cls), **kwargs)

def UkSidebar(sections, headers=None, outer_margin=4, inner_margin=4, cls=(), **kwargs):
    assert headers is None or len(headers)==len(sections)
    sidebar_content = map(lambda s_h: UkSidebarSection(*s_h, **kwargs), zip_longest(sections, tuplify(headers)))
    return Div(cls=f"space-y-{inner_margin} p-{outer_margin} " + stringify(cls))(*sidebar_content)

# %% ../lib_nbs/00_core.ipynb
def Card(*c, # Components that go in the body
        header=None, # Components that go in the header
        footer=None,  # Components that go in the footer
        body_cls='space-y-6', # classes for the body
        header_cls=(), # classes for the header
        footer_cls=(), # classes for the footer
        cls=(), #class for outermost component
        **kwargs # classes that for the card itself
        ):
    header_cls, footer_cls, body_cls, cls = map(stringify, (header_cls, footer_cls, body_cls, cls))
    res = []
    if header: res += [Div(cls='uk-card-header ' + header_cls)(header),]
    res += [Div(cls='uk-card-body ' + body_cls)(*c),]
    if footer: res += [Div(cls='uk-card-footer ' + footer_cls)(footer),]
    return Div(cls='uk-card '+cls, **kwargs)(*res)

# %% ../lib_nbs/00_core.ipynb
def UkModalTitle(*c, cls=()): return Div(cls='uk-modal-title ' + stringify(cls))(*c)

def Modal(*c,
        header=None, # Components that go in the header
        footer=None,  # Components that go in the footer
        body_cls='space-y-6', # classes for the body
        header_cls='p-6', # classes for the header
        footer_cls=(), # classes for the footer
        cls=(), #class for outermost component
        **kwargs # classes that for the card itself
        ):
    header_cls, footer_cls, body_cls, cls = map(stringify, (header_cls, footer_cls, body_cls, cls))
    res = []
    if header: res += [Div(cls='uk-modal-header ' + header_cls)(header),]
    res += [Div(cls='uk-modal-body uk-modal-dialog ' + body_cls)(*c),]
    if footer: res += [Div(cls='uk-modal-footer ' + footer_cls)(footer),]
    return Div(cls='uk-modal uk-modal-container' + cls, uk_modal=True, **kwargs)(*res)


# %% ../lib_nbs/00_core.ipynb
def _default_cell(col, row): return Td(row[col], cls='p-2')

# %% ../lib_nbs/00_core.ipynb
def TableHeader(columns, header_render=None):
    rndr = header_render or Th(cls='p-2')
    return Tr(*map(rndr, columns))

# %% ../lib_nbs/00_core.ipynb
def TableRow(row, columns, cell_render=None):
    rndr = cell_render or _default_cell
    return Tr(*[rndr(col, row) for col in columns])

# %% ../lib_nbs/00_core.ipynb
def UkTable(columns, data, *args, cls=(), footer=None, cell_render=None, header_render=None, **kwargs):
    # table middle, small : Should these be parameterized?
    # Document, especially cell and header render
    table_cls = 'uk-table uk-table-middle uk-table-divider uk-table-hover uk-table-small ' + stringify(cls)
    head = Thead(TableHeader(columns, header_render))
    body = Tbody(*[TableRow(d, columns, cell_render) for d in data])
    if footer: table_content.append(Tfoot(footer))
    return Table(cls=table_cls, *args, **kwargs)(*[head,body])

# %% ../lib_nbs/00_core.ipynb
def UkFormSection(title, description, *c, button_txt='Update', outer_margin=6, inner_margin=6):
    return Div(cls=f'space-y-{inner_margin} py-{outer_margin}')(
        Div(UkH3(title), P(description, cls=TextT.medium_sm)),
        UkHSplit(), *c,
        Div(UkButton(button_txt, cls=UkButtonT.primary)) if button_txt else None)
