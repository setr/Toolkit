set nocompatible              " be iMproved, required
filetype off                  " required

" set the runtime path to include Vundle and initialize
set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()
" alternatively, pass a path where Vundle should install plugins
"call vundle#begin('~/some/path/here')


" install vundle with: git clone https://github.com/gmarik/Vundle.vim.git ~/.vim/bundle/Vundle.vim
" Vundle will handle the rest, with :PluginInstall
" let Vundle manage Vundle, required
Plugin 'gmarik/Vundle.vim'
Plugin 'tpope/vim-surround'			    " <action>s to select surrounding characters
Plugin 'junegunn/vim-easy-align' 		"Auto-Alignment
Plugin 'scrooloose/nerdcommenter'		"Auto-Commenter
Plugin 'justinmk/vim-sneak'             " s to search 2 chars
Plugin 'romainl/Apprentice'

" All of your Plugins must be added before the following line
call vundle#end()                       " required
filetype plugin indent on               " required
" To ignore plugin indent changes, instead use:
"filetype plugin on
"
" Brief help
" :PluginList       - lists configured plugins
" :PluginInstall    - installs plugins; append `!` to update or just :PluginUpdate
" :PluginSearch foo - searches for foo; append `!` to refresh local cache
" :PluginClean      - confirms removal of unused plugins; append `!` to auto-approve removal

" # = number, ',' = leader, _ = space
" NerdCommenter
    " #,cc comments the current line
    " #,c_ toggles line comment

" Surround

" Easy-Align

colorscheme apprentice

"set cursorline                              " hilight cursor line
set more                                    " ---more--- like less
set number                                  " line numbers
set scrolloff=3                             " lines above/below cursor
set showcmd                                 " show cmds being typed
set title                                   " window title
set vb t_vb=                                " disable beep and flashing
set wildignore=*.a,*.o,*.so,*.pyc,*.jpg,
                     \*.jpeg,*.png,*.gif,*.pdf,*.git,
                     \*.swp,*.swo                    " tab completion ignores
set wildmenu                                " better auto complete
set wildmode=longest,list                   " bash-like auto complete
set nostartofline                               " keep cursor column pos

" softwrap
set wrap                                      " don't wrap lines
set linebreak
set nolist
set textwidth=0
set wrapmargin=0
"

set numberwidth=3                               " 999 lines
set shortmess+=I                                " disable startup message
set splitbelow                                  " splits go below w/focus
set splitright                                  " vsplits go right w/focus
set ttyfast                                     " for faster redraws etc

 """ Folding {{{
        set foldcolumn=0                            " hide folding column
        set foldmethod=indent                       " folds using indent
        set foldnestmax=10                          " max 10 nested folds
        set foldlevelstart=99                       " folds open by default
    """ }}}
    """ Search and replace {{{
        set gdefault                                " default s//g (global)
        set incsearch                               " "live"-search
    """ }}}
    """ Matching {{{
        set matchtime=2                             " time to blink match {}
        set matchpairs+=<:>                         " for ci< or ci>
        set showmatch                               " tmpjump to match-bracket
    """ }}}
    """ Return to last edit position when opening files {{{
        augroup LastPosition
            autocmd! BufReadPost *
                \ if line("'\"") > 0 && line("'\"") <= line("$") |
                \     exe "normal! g`\"" |
                \ endif
        augroup END
    """ }}}
""" Files {{{
    set autochdir                                   " always use curr. dir.
    set autoread                                    " refresh if changed
    set confirm                                     " confirm changed files
    set noautowrite                                 " never autowrite
    set nobackup                                    " disable backups
    """ Persistent undo. Requires Vim 7.3 {{{
        if has('persistent_undo') && exists("&undodir")
            set undodir=$HOME/.vim/undo/            " where to store undofiles
            set undofile                            " enable undofile
            set undolevels=500                      " max undos stored
            set undoreload=10000                    " buffer stored undos
        endif
    """ }}}

""" Text formatting {{{
    set autoindent                                  " preserve indentation
    set backspace=indent,eol,start                  " smart backspace
    set cinkeys-=0#                                 " don't force # indentation
    set expandtab                                   " no real tabs
    set ignorecase                                  " by default ignore case
    set nrformats+=alpha                            " incr/decr letters C-a/-x
    set shiftround                                  " be clever with tabs
    set shiftwidth=4                                " default 8
    set smartcase                                   " sensitive with uppercase
    set smarttab                                    " tab to 0,4,8 etc.
    set softtabstop=4                               " "tab" feels like <tab>
    set tabstop=4                                   " replace <TAB> w/4 spaces
    """ Only auto-comment newline for block comments {{{
        augroup AutoBlockComment
            autocmd! FileType c,cpp setlocal comments -=:// comments +=f://
        augroup END
    """ }}}

""" Keybindings {{{
    """ General {{{
        " Remap <leader>
        let mapleader=","

        " Quickly edit/source .vimrc
        noremap <leader>ve :edit $HOME/.vimrc<CR>
        noremap <leader>vs :source $HOME/.vimrc<CR>

        " Yank(copy) to system clipboard
        noremap <leader>y "+y

        " Toggle folding
        nnoremap <silent> <Space> @=(foldlevel('.')?'za':"\<Space>")<CR>
        vnoremap <Space> zf
        " Scroll up/down lines from 'scroll' option, default half a screen
        map <C-j> <C-d>
        map <C-k> <C-u>

        " Treat wrapped lines as normal lines
        nnoremap j gj
        nnoremap k gk

        " Disable annoying ex mode (Q)
        map Q <nop>
