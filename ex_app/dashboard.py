"""FrankenUI Dashboard Example"""

# AUTOGENERATED! DO NOT EDIT! File to edit: ../ex_nbs/03_dashboard.ipynb.

# %% auto 0
__all__ = ['rev', 'sub', 'sal', 'act', 'top_info_row', 'recent_sales', 'teams', 'opt_hdrs', 'team_dropdown', 'hotkeys', 'logout',
           'user', 'avatar', 'avatar_dropdown', 'top_nav', 'dashboard_homepage', 'InfoCard', 'AvatarItem',
           'generate_chart', 'space', 'page']

# %% ../ex_nbs/03_dashboard.ipynb
from fasthtml.common import *
from fh_frankenui import *
from fasthtml.svg import *
from fh_matplotlib import matplotlib2fasthtml
import numpy as np
import matplotlib.pylab as plt

# %% ../ex_nbs/03_dashboard.ipynb
def InfoCard(title, value, change):
    return Div(Card(
             Div(UkH3(value),
                P(change, cls=TextT.muted_sm)),
             header = UkH4(title),))

# %% ../ex_nbs/03_dashboard.ipynb
rev = InfoCard("Total Revenue", "$45,231.89", "+20.1% from last month")
sub = InfoCard("Subscriptions", "+2350", "+180.1% from last month")
sal = InfoCard("Sales", "+12,234", "+19% from last month")
act = InfoCard("Active Now", "+573", "+201 since last hour")

# %% ../ex_nbs/03_dashboard.ipynb
top_info_row = Grid(rev,sub,sal,act,cols=4, cls=GridT.small)

# %% ../ex_nbs/03_dashboard.ipynb
def AvatarItem(name, email, amount):
    return Div(cls="flex items-center")(
        DiceBearAvatar(name, 9,9),
        Div(cls="ml-4 space-y-1")(
            P(name, cls=TextT.medium_sm),
            P(email, cls=TextT.muted_sm)),
        Div(amount, cls="ml-auto font-medium"))

recent_sales = Card(
    Div(cls="space-y-8")(
        *[AvatarItem(n,e,d) for (n,e,d) in (
            ("Olivia Martin",   "olivia.martin@email.com",   "+$1,999.00"),
            ("Jackson Lee",     "jackson.lee@email.com",     "+$39.00"),
            ("Isabella Nguyen", "isabella.nguyen@email.com", "+$299.00"),
            ("William Kim",     "will@email.com",            "+$99.00"),
            ("Sofia Davis",     "sofia.davis@email.com",     "+$39.00"))]),
    header=Div(
        UkH3("Recent Sales"),
        P("You made 265 sales this month.", cls=TextT.muted_sm)),

cls='lg:col-span-3')

# %% ../ex_nbs/03_dashboard.ipynb
@matplotlib2fasthtml
def generate_chart(num_points):
    plotdata = [np.random.exponential(1) for _ in range(num_points)]
    plt.plot(range(len(plotdata)), plotdata)

# %% ../ex_nbs/03_dashboard.ipynb
teams = [
    ["Alicia Koch"],
    ['Acme Inc', 'Monster Inc.'],
    ['Create a Team']
]

opt_hdrs = ["Personal", "Team", ""]

team_dropdown = UkDropdownButton(*map(lambda t: map(A, t), teams),
    opt_hdrs=opt_hdrs,
    label=teams[0][0])

# %% ../ex_nbs/03_dashboard.ipynb
hotkeys = [('Profile','⇧⌘P'),('Billing','⌘B'),('Settings','⌘S'),('New Team', '')]

def space(*c): return A(FullySpacedDiv(*c, wrap_tag=P))

hotkeys = tuple(map(lambda x: space(*x), hotkeys))
logout = space('Logout' ,''),
user = Li(cls='px-2 py-1.5 text-sm')(
        Div(cls='flex flex-col space-y-1')(
            P('sveltecult', cls='text-sm font-medium leading-none'),
            P('leader@sveltecult.com', cls='text-xs leading-none text-muted-foreground'))),
avatar = DiceBearAvatar('Alicia Koch',8,8)
avatar_dropdown = UkDropdownButton(user,hotkeys,logout,
    label=avatar)

show(avatar_dropdown)

# %% ../ex_nbs/03_dashboard.ipynb
top_nav = UkNavbar(
    lnav=[team_dropdown, Li(A("Overview")), Li(A("Customers")), Li(A("Products")), Li(A("Settings"))],
    rnav=[UkInput(placeholder='Search'), avatar_dropdown],
)

# %% ../ex_nbs/03_dashboard.ipynb
def page():
    return Div(cls="space-y-4")(
        Div(cls="border-b border-border px-4")(top_nav),
        UkH2('Dashboard'),
        UkTab("Overview", "Analytics", "Reports", "Notifications"), 
        top_info_row,
        Grid(Card(generate_chart(10),cls='lg:col-span-4'),
            recent_sales,
            gap=4,cls='lg:grid-cols-7'))

# %% ../ex_nbs/03_dashboard.ipynb
dashboard_homepage = page()
