"""FrankenUI Tasks Example"""

# AUTOGENERATED! DO NOT EDIT! File to edit: ../ex_nbs/01_tasks.ipynb.

# %% auto 0
__all__ = ['priority_dd', 'rows_per_page_dd', 'status_dd', 'hotkeys_a', 'hotkeys_b', 'avatar_opts', 'page_heading',
           'table_controls', 'task_columns', 'tasks_table', 'tasks_ui', 'tasks_homepage', 'create_hotkey_li',
           'CreateTaskModal', 'checkbox', 'task_dropdown', 'header_render', 'cell_render', 'footer']

# %% ../ex_nbs/01_tasks.ipynb
from fasthtml.common import *
from fh_frankenui import *
from fasthtml.svg import *
import json

# %% ../ex_nbs/01_tasks.ipynb
with open('data/status_list.json', 'r') as f: data     = json.load(f)
with open('data/statuses.json',    'r') as f: statuses = json.load(f)

# %% ../ex_nbs/01_tasks.ipynb
priority_dd = [{'priority': "low", 'count': 36 }, {'priority': "medium", 'count': 33 }, {'priority': "high", 'count': 31 }]

rows_per_page_dd = [10,20,30,40,50]

status_dd = [{'status': "backlog", 'count': 21 },{'status': "todo", 'count': 21 },{'status': "progress", 'count': 20 },{'status': "done",'count': 19 },{'status': "cancelled", 'count': 19 }]


# %% ../ex_nbs/01_tasks.ipynb
def create_hotkey_li(hotkey):
    return Li(A(cls='uk-drop-close justify-between')(
        hotkey[0],
        Span(hotkey[1], cls='ml-auto text-xs tracking-widest opacity-60')))

hotkeys_a = (('Profile','⇧⌘P'),('Billing','⌘B'),('Settings','⌘S'),('New Team',''))
hotkeys_b = (('Logout',''), )

# TODO convert to navbar
avatar_opts = Ul(cls='uk-dropdown-nav uk-nav')(
    Li(cls='px-2 py-1.5 text-sm')(
        Div(cls='flex flex-col space-y-1')(
            P('sveltecult', cls='text-sm font-medium leading-none'),
            P('leader@sveltecult.com', cls='text-xs leading-none text-muted-foreground'))),
    Li(cls='uk-nav-divider'),
    *map(create_hotkey_li, hotkeys_a),
    Li(cls='uk-nav-divider'),
    *map(create_hotkey_li, hotkeys_b)
)

# %% ../ex_nbs/01_tasks.ipynb
def CreateTaskModal():
    return Modal(
        Div(cls='p-6')(
            UkModalTitle('Create Task'),P('Fill out the information below to create a new task', cls=TextT.muted_sm),
            Br(),
            Form(cls='space-y-6')(
                Grid(UkSelect(*Options('Documentation', 'Bug', 'Feature'), label='Task Type', id='task_type'),
                     UkSelect(*Options('In Progress', 'Backlog', 'Todo', 'Cancelled', 'Done'), label='Status', id='task_status'),
                     UkSelect(*Options('Low', 'Medium', 'High'), label='Priority', id='task_priority')),
                UkTextArea(label='Title', placeholder='Please describe the task that needs to be completed'),
                Div(cls='flex justify-end space-x-2')(
                    UkButton(cls=UkButtonT.ghost + ' uk-modal-close')('Cancel'),
                    UkButton(cls=UkButtonT.primary + ' uk-modal-close')('Submit')))),
        id='TaskForm')

# %% ../ex_nbs/01_tasks.ipynb
page_heading =SpaceBetweenDiv(cls='space-y-2')(
            Div(cls='space-y-2')(
                UkH2('Welcome back!'),P("Here's a list of your tasks for this month!", cls=TextT.muted_sm)),
            Div(A(href='#', cls='h-8 w-8 inline-flex rounded-full bg-accent ring-ring')(Img(src='https://api.dicebear.com/8.x/lorelei/svg?seed=sveltecult')),
                Div(uk_dropdown='mode: click; pos: bottom-right', cls='uk-dropdown uk-drop')(avatar_opts)))

# %% ../ex_nbs/01_tasks.ipynb
table_controls =(UkInput(cls='w-[250px]',placeholder='Filter task'),
     UkDropdownButton(
         [A(FullySpacedDiv(a['status'], a['count'], wrap_tag=P),cls='capitalize') for a in status_dd],
         label = "Status", 
         btn_cls=(TextT.medium_xs, 'uk-button-default')),     
     UkDropdownButton(
         [A(FullySpacedDiv(LAlignedIconTxt(a['priority'], icon="check"), a['count']),cls='capitalize') for a in priority_dd],                         
         label = "Priority", 
         btn_cls=(TextT.medium_xs,'uk-button-default')),
      UkDropdownButton([A(LAlignedIconTxt(o, icon="check")) for o in ['Title','Status','Priority']],
            label='View',
            opt_hdrs=["Toggle Columns"],
            btn_cls=(TextT.medium_xs,'uk-button-default')),
            UkButton('Create Task',cls=('uk-button-primary', TextT.medium_xs), uk_toggle="target: #TaskForm"))

# %% ../ex_nbs/01_tasks.ipynb
def checkbox(selected=False, ):
    # TODO: Use UkCheckbox Type
    if selected: return Input(type='checkbox', cls='uk-checkbox', checked=True)
    return              Input(type='checkbox', cls='uk-checkbox')

# %% ../ex_nbs/01_tasks.ipynb
def task_dropdown():
    # TODO: Figure out uk-drop-close boilerplate fix
    return UkDropdownButton([
            A('Edit',                   cls='uk-drop-close'),
            A('Make a copy',            cls='uk-drop-close'),
            A('Favorite',               cls='uk-drop-close')],
            [A(SpacedPP('Delete', '⌘⌫'), cls='uk-drop-close')])

# %% ../ex_nbs/01_tasks.ipynb
def header_render(col):
    cls = 'p-2 ' + 'uk-table-shrink' if col in ('Done','Actions') else ''
    match col:
        case "Done":    return Th(checkbox, cls=cls)
        case 'Actions': return Th("",       cls=cls)
        case _:         return Th(col, cls=cls)

# %% ../ex_nbs/01_tasks.ipynb
def cell_render(col, row):
    def _Td(*args,cls='', **kwargs): return Td(*args, cls=f'p-2 {cls}',**kwargs)
    match col:
        case "Done":  return _Td(cls='uk-table-shrink')(checkbox(row['selected']))
        case "Task":  return _Td(row["id"])
        case "Title": return _Td(cls='uk-table-expand max-w-[500px] truncate')(row["title"], cls='font-medium')
        case "Status" | "Priority": return _Td(cls='uk-text-nowrap uk-text-capitalize')(Span(row[col.lower()]))
        case "Actions": return _Td(cls='uk-table-shrink')(task_dropdown())
        case _: raise ValueError(f"Unknown column: {col}")

# %% ../ex_nbs/01_tasks.ipynb
task_columns = ["Done", 'Task', 'Title', 'Status', 'Priority', 'Actions']

tasks_table = Div(cls='uk-overflow-auto mt-4 rounded-md border border-border')(UkTable(
    columns=task_columns,
    data=data,
    cell_render=cell_render,
    header_render=header_render,))

# %% ../ex_nbs/01_tasks.ipynb
def footer():
    hw_cls = 'h-4 w-4'
    return SpaceBetweenDiv(cls='mt-4 px-2 py-2')(
        Div('1 of 100 row(s) selected.', cls='flex-1 text-sm text-muted-foreground'),
        Div(cls='flex flex-none items-center space-x-8')(
            CenteredDiv('Page 1 of 10', cls='w-[100px] text-sm font-medium'),
            LAlignedDiv(
                UkIconButton(cls='hidden lg:inline-flex')(Span('Go to last page', cls='sr-only'),
                    Span(uk_icon='chevron-double-left', cls=hw_cls)),
                UkIconButton(Span('Go to previous page', cls='sr-only'),
                    Span(uk_icon='chevron-left', cls=hw_cls)),
                UkIconButton(Span('Go to next page', cls='sr-only'),
                    Span(uk_icon='chevron-right', cls=hw_cls)),
                UkIconButton(cls='hidden lg:inline-flex')(
                    Span('Go to last page', cls='sr-only'),
                    Span(uk_icon='chevron-double-right', cls=hw_cls)),
            gap=2)))

# %% ../ex_nbs/01_tasks.ipynb
tasks_ui = Div(
    SpaceBetweenDiv(cls='mt-8')(
        Div(cls='flex flex-1 gap-4')(table_controls)),
    tasks_table,
    footer(),)

# %% ../ex_nbs/01_tasks.ipynb
tasks_homepage = CreateTaskModal(), Div(cls='p-8')(page_heading, tasks_ui)
